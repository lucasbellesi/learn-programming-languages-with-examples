# Beta validation — September 7, 2026

The Sandbox feasibility gate passed on real Vercel Hobby infrastructure using SDK
3.2.1 and curriculum commit `ab6db796a3f864399bce264455f58619d05b7274`.

## Execution

- All 48 foundations examples and 96 foundations reference solutions passed their
  canonical Python contracts in fresh sandboxes. No reference implementation is
  executed when grading a learner submission.
- Measured end-to-end attempts ranged from 1.480 to 18.801 seconds, with a median
  of 4.458 seconds, using two test workers. These are observations, not guarantees.
- The retained snapshot occupies 1,065,920,936 bytes. Superseded test snapshots
  were deleted after the replacement passed the six-language and isolation suite.
- Toolchains: GCC 11.5 with C++17, .NET SDK 8.0.424, Go 1.22.12, Corretto Java
  21.0.12, Python 3.12.13, Node 22.22.2, and TypeScript 5.9.3 from the root lockfile.
- Infinite loops, excessive output, compilation errors, cancellation, unprivileged
  execution, blocked outbound TCP, inaccessible supervisor inputs, and incomplete
  starters produced their expected outcomes.

## Application and database

- Real browser-to-API-to-Sandbox runs succeeded with Supabase admission enabled.
- An incomplete Python starter displayed individual expected/actual case failures;
  an edited solution passed its three cases.
- GitHub OAuth was completed. Three local drafts were imported. Imported progress
  did not create server-verified progress; a subsequent authenticated successful
  check created one verified progress record.
- PostgreSQL tests cover guest/account/IP limits, global and per-identity slots,
  idempotency, expiry, cancellation races, RLS isolation, and rejection of forged
  progress and unprivileged quota calls.
- Browser tests cover concept-preserving language navigation, editing and reload,
  hints, disabled execution, execution feedback, mobile panel switching, and
  navigation warnings with downloads when browser storage fails. Cloud responses in CI are
  mocked; the real integration checks above run only in a trusted environment.
- Root `verify-repo` passed: 62 automation tests, 149 example jobs, 881 exercise
  jobs, 48 checkpoint solutions, and uncovered C++/Java builds. Root `lint` passed.

## Security runtime validation — November 14, 2026

Validated candidate: `snap_hRVmWrp8B3oybHRzftriYThDW4Wk`, built from trusted commit
`97cfcfe5fa3e37f8d03fcf37c5e31aaa997b70b4`. Size: 1,189,540,682 bytes. The runtime
metadata is recorded in `content/execution-runtime.json` and execution rejects
other configured snapshot IDs. This candidate is selected locally; production
settings have not been promoted by this validation.

- All 48 foundations examples and 96 reference solutions passed their canonical
  contracts in fresh sandboxes with two test workers.
- Seven additional scenarios produced their expected outcomes: infinite loop,
  excessive output, compilation error, cancellation, unprivileged execution with
  protected files/no credentials/private runtime IPC, blocked network, and an
  incomplete starter. Total: **151 checks, zero unexpected failures**.
- Measured attempts ranged from 1.249 to 27.270 seconds, median 3.622 seconds.
  These are observations from this run, not runtime guarantees.
- Inventory: GCC 11.5.0, .NET SDK 8.0.428 / runtime 8.0.34, Go 1.27.4, Corretto
  21.0.12.1, Python 3.12.14, Node 22.23.4, and TypeScript 5.9.3.
- The official Go Linux archive SHA-256 was verified before installation.
- The first candidate failed .NET user-scoped IPC initialization because the
  system `nobody` account has `/` as its passwd home. A per-case, private,
  learner-owned `XDG_RUNTIME_DIR` fixed the real supervisor run. The snapshot
  recipe now requires an isolated C# bootstrap to pass before saving an image.
  UID 65534, PID/network namespaces, deny-all networking, and protected oracle
  files remain in place. The rejected candidate was deleted.
- This suite uses the real provider and supervisor directly. It does not replace
  browser-to-API OAuth/Supabase integration or review of production settings.

Local regression validation also passed: 20 security probe groups including local
HTTP/Chromium, 40 browser cases across Chromium/Firefox/mobile, 8 web unit/database
tests, production build, typecheck, formatting, npm audits, and full root checks.

## Release boundary

Production credentials are scoped only to Vercel Production. The production
domain is `programming-examples.vercel.app`, with `master` as the production branch.
Previews permit reading and local editing; they do not execute or synchronize.
Production publication requires the separately authorized merge of the PR.

Free capacity is shared and can be exhausted. A paused Supabase project disables
execution and sync. Later cloud draft updates currently use the explicit **Sync
drafts** action; local saving is automatic. Scheduled retention cleanup resumes
when a paused Free database wakes.
