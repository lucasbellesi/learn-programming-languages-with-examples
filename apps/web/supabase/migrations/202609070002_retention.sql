-- Keep cleanup independent of traffic. Paused Free databases resume it on wake.
create extension if not exists pg_cron;
alter table public.executions alter column expires_at
  set default now() + interval '55 seconds';

select cron.schedule('learning-result-retention', '*/5 * * * *', $$
  delete from public.executions where created_at < now() - interval '7 days';
  delete from public.execution_quotas where day < current_date - 1;
  delete from cron.job_run_details
    where jobid in (select jobid from cron.job where jobname = 'learning-result-retention')
      and end_time < now() - interval '7 days';
$$);
