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

## Release boundary

Production credentials are scoped only to Vercel Production. The production
domain is `programming-examples.vercel.app`, with `master` as the production branch.
Previews permit reading and local editing; they do not execute or synchronize.
Production publication requires the separately authorized merge of the PR.

Free capacity is shared and can be exhausted. A paused Supabase project disables
execution and sync. Later cloud draft updates currently use the explicit **Sync
drafts** action; local saving is automatic. Scheduled retention cleanup resumes
when a paused Free database wakes.
