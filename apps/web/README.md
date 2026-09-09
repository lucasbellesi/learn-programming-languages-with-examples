# Code by Example

A Next.js learning site built from the repository's canonical curriculum. The
catalog includes all six languages, 144 modules, 288 exercises, and 48 checkpoints.
The first online execution release covers 48 examples and 96 foundations exercises.
Other levels and checkpoints remain readable and downloadable.

## Local development

Requires Node 22, npm, Python 3, and Git. From this directory:

```bash
npm ci
npm run dev
```

Open the local URL printed by Next.js. No cloud credentials are needed to read,
search, edit, save drafts in IndexedDB, download code, or reveal reference solutions.
Execution fails closed when its environment or quota database is unavailable.

```bash
npm test
npm run build
npm run typecheck
npm run lint
```

Also run the root repository verification and lint scripts before opening a PR.
`generated/` is rebuilt from the manifests, Markdown, starter files, and source code.
It must not be committed. The exported commit identifies the content revision.

## Vercel and Supabase setup

1. Use Vercel Hobby for this personal, noncommercial project. Configure the Vercel
   project with `apps/web` as its root, Next.js as its framework, and access to
   source files outside the root directory. Production tracks `master`; PRs get previews.
2. Create a dedicated Supabase Free project. Apply
   [the schema migration](supabase/migrations/202609070001_learning_beta.sql) and
   [retention migration](supabase/migrations/202609070002_retention.sql) using the SQL
   editor. It enables RLS and grants table access explicitly. There are no public
   execution-table policies: only the server service role can admit or finish jobs.
3. Configure GitHub OAuth in Supabase. Use Supabase's displayed callback URL when
   registering the OAuth app. Allow only the site's trusted callback URLs under
   `/auth/callback`, including localhost for development. Do not allow arbitrary
   third-party redirect domains.
4. Copy `.env.example` to `.env.local` and fill the public Supabase URL/key, server
   service key, and a randomly generated session secret of at least 32 bytes.
   Keep service keys out of `NEXT_PUBLIC_*` variables. Add hosted values through
   Vercel environment settings; credentials must never be committed.
5. Authenticate with Vercel CLI, link this project, and run `vercel env pull` to get
   a local OIDC token. Run `npm run sandbox:probe -- --snapshot` to prepare a trusted
   snapshot. Copy the reported snapshot ID into `SANDBOX_SNAPSHOT_ID`.
6. Run `npm run test:sandbox`. Only enable `EXECUTION_ENABLED=true` after the
   integration suite passes and the database and OAuth configuration are verified.
   Preview deployments without secrets deliberately disable execution and sync.

Keep Sandbox usage in the free tier. This site does not purchase services or
upgrade plans. Exhausted quota pauses execution. Supabase may pause a Free project
after inactivity; reading, editing, and downloads must still work.

## Execution and data boundaries

The API accepts an activity ID, content revision, code, stdin, `run/check` mode, and
an idempotency key. It selects entrypoints, support files, commands, and expected
outputs from trusted content. Clients cannot send shell commands or grading rules.

A PostgreSQL transaction admits at most four concurrent jobs, one per identity.
Guests get five requests per day per signed session and ten per hashed IP; signed-in
users get 25 per day. Admission consumes quota even if startup subsequently fails.
IP hashes rotate daily. Cleanup runs on admission and through a five-minute
database Cron job, deleting detailed results older than seven days. A paused
database resumes cleanup when it wakes. Completion records include language and
wall-clock duration; provider resource consumption is available in Vercel usage.

Each request creates a nonpersistent microVM with one vCPU, 2 GiB memory, no public
ports, and Vercel's deny-all network policy. A root-owned Python supervisor starts
each compilation/case as UID 65534 using fresh PID and network namespaces with
`no-new-privs`. The learner cannot write the supervisor, its inputs, or results.
PID namespaces remove descendants, including detached children, between cases.
The canonical Python output oracle evaluates captured output outside the learner
process. Only runtime artifacts are copied into fresh case directories.

Limits: 64 KiB code, 16 KiB stdin, 64 KiB combined output per case, 30 seconds to compile,
3 seconds per case, and a 55-second execution deadline. Console output is monitored
and truncated independently of artifact size. .NET needs large anonymous memfd
reservations, so `RLIMIT_FSIZE` is not applied to dotnet; the microVM remains the
outer storage/memory boundary. No additional packages can be installed during runs.

Root-owned result files are retrieved through the SDK filesystem API rather than
printed to service logs. The HTTP request ends after starting a detached command;
subsequent authenticated polls retrieve results. Cancellation and completion are
serialized in PostgreSQL so a late poll cannot overwrite a cancelled job. An
abandoned browser cannot keep a microVM alive beyond its deadline.

IndexedDB holds local drafts and local completion. Sign-in imports drafts, with an
explicit choice when device and cloud copies differ. Cloud writes use timestamp
preconditions to detect concurrent edits. Imported completion is stored separately
from server-verified progress; neither is a credential or certificate. Use **Sync
drafts** to upload later local changes. Detailed execution history is not a backup
of learner source files.

## Maintaining snapshots

See [the beta validation record](VALIDATION.md) for measured integration results
and the release boundary. The editor assets are served locally from the pinned
Monaco package; no editor CDN is required. Run `npm run test:browser` after
`npx playwright install chromium` to check browser workflows without cloud access.

`scripts/sandbox-probe.mjs` installs and measures the six toolchains on trusted
repository code. Its report is in `build/sandbox-feasibility.json`.
`scripts/refresh-snapshot.mjs` installs a changed supervisor into a new version of
an existing snapshot and updates the local snapshot ID. It never edits a running
learner environment. Record and test the new version before updating hosted settings.
Delete superseded snapshots after verification to stay within free storage quotas.

`npm run test:sandbox` checks every foundations example/reference solution, plus
timeouts, output limits, compilation failure, cancellation, unprivileged execution,
network denial, and incomplete starters. It consumes Sandbox quota and must run only
from a trusted checkout. PR CI runs catalog/database tests and the build without
cloud secrets; never inject execution credentials into untrusted fork code.
