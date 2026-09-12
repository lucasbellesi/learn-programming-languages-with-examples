-- Apply to a dedicated Supabase Free project. Never use the service key in a browser.
create table public.drafts (
  user_id uuid not null references auth.users(id) on delete cascade,
  activity_id text not null,
  code text not null check (octet_length(code) <= 65536),
  revision text not null,
  imported_passed boolean not null default false,
  updated_at timestamptz not null default now(),
  primary key (user_id, activity_id)
);
alter table public.drafts enable row level security;
create policy own_drafts on public.drafts for all to authenticated
  using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
grant select, insert, update, delete on public.drafts to authenticated;

create table public.progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  activity_id text not null,
  revision text not null,
  verified_at timestamptz not null default now(),
  primary key (user_id, activity_id, revision)
);
alter table public.progress enable row level security;
create policy read_own_progress on public.progress for select to authenticated
  using ((select auth.uid()) = user_id);
grant select on public.progress to authenticated;

create table public.executions (
  id uuid primary key default gen_random_uuid(),
  identity text not null,
  user_id uuid references auth.users(id) on delete cascade,
  request_key uuid not null,
  request_hash text not null,
  activity_id text not null,
  revision text not null,
  mode text not null check (mode in ('run','check')),
  status text not null default 'starting',
  sandbox_id text,
  command_id text,
  result jsonb,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null default now() + interval '65 seconds',
  unique(identity, request_key)
);
alter table public.executions enable row level security;
-- All execution access goes through the server with explicit ownership checks.
create index executions_active on public.executions(expires_at) where status in ('starting','compiling','running');
create table public.execution_quotas (
  bucket text not null,
  day date not null default current_date,
  used integer not null default 0,
  primary key (bucket, day)
);
alter table public.execution_quotas enable row level security;
grant all on public.drafts, public.progress, public.executions, public.execution_quotas to service_role;

create function public.reserve_execution(
  p_identity text, p_user_id uuid, p_ip text, p_key uuid, p_hash text,
  p_activity text, p_revision text, p_mode text
) returns jsonb language plpgsql security definer set search_path = public as $$
declare existing public.executions; created public.executions; identity_used integer; ip_used integer;
begin
  -- One transaction serializes admission across all stateless Vercel instances.
  perform pg_advisory_xact_lock(78190421);
  select * into existing from executions where identity=p_identity and request_key=p_key;
  if found then
    if existing.request_hash <> p_hash then raise exception 'Idempotency key conflicts with a different request'; end if;
    return jsonb_build_object('execution',to_jsonb(existing),'created',false);
  end if;
  update executions set status='limit', result=jsonb_build_object('status','limit','message','Execution expired')
    where expires_at < now() and status in ('starting','compiling','running');
  delete from executions where created_at < now() - interval '7 days';
  delete from execution_quotas where day < current_date - 1;
  if (select count(*) from executions where status in ('starting','compiling','running')) >= 4 then
    raise exception 'All execution slots are busy. Please try again shortly';
  end if;
  if exists(select 1 from executions where identity=p_identity and status in ('starting','compiling','running')) then
    raise exception 'An execution is already running for this session';
  end if;
  select used into identity_used from execution_quotas where bucket=p_identity and day=current_date;
  if coalesce(identity_used,0) >= (case when p_user_id is null then 5 else 25 end) then
    raise exception 'Daily execution limit reached. Editing and downloads remain available';
  end if;
  if p_user_id is null then
    if p_ip is null then raise exception 'Cannot verify guest quota'; end if;
    select used into ip_used from execution_quotas where bucket=p_ip and day=current_date;
    if coalesce(ip_used,0) >= 10 then raise exception 'Guest network daily limit reached'; end if;
    insert into execution_quotas(bucket,used) values(p_ip,1)
      on conflict(bucket,day) do update set used=execution_quotas.used+1;
  end if;
  insert into execution_quotas(bucket,used) values(p_identity,1)
    on conflict(bucket,day) do update set used=execution_quotas.used+1;
  insert into executions(identity,user_id,request_key,request_hash,activity_id,revision,mode)
    values(p_identity,p_user_id,p_key,p_hash,p_activity,p_revision,p_mode) returning * into created;
  return jsonb_build_object('execution',to_jsonb(created),'created',true);
end $$;
revoke all on function public.reserve_execution(text,uuid,text,uuid,text,text,text,text) from public, anon, authenticated;
grant execute on function public.reserve_execution(text,uuid,text,uuid,text,text,text,text) to service_role;

create function public.finish_execution(p_id uuid, p_identity text, p_result jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare current_execution public.executions;
begin
  select * into current_execution from executions where id=p_id and identity=p_identity for update;
  if not found then raise exception 'Execution not found'; end if;
  if current_execution.status not in ('starting','compiling','running') then
    return current_execution.result;
  end if;
  update executions set status=p_result->>'status',result=p_result where id=p_id;
  if p_result->>'status'='passed' and current_execution.mode='check' and current_execution.user_id is not null then
    insert into progress(user_id,activity_id,revision)
      values(current_execution.user_id,current_execution.activity_id,current_execution.revision)
      on conflict(user_id,activity_id,revision) do update set verified_at=now();
  end if;
  return p_result;
end $$;
revoke all on function public.finish_execution(uuid,text,jsonb) from public,anon,authenticated;
grant execute on function public.finish_execution(uuid,text,jsonb) to service_role;
