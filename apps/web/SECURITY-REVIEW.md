# OWASP Top 10 security assessment — November 14, 2026

## Result and scope

Assessed revision: `e34366857ed93284f9bc79e80faa94ce28b48164`.
Reference: [OWASP Top 10:2025](https://top10.owasp.org/2025/).

This is a source-assisted, local assessment of the learning site, not a complete
external penetration test or a production security certification. The assessment
found **four medium-priority issues and two low-priority issues**. No critical or
high-severity exploit was demonstrated within the tested scope. Findings remain
open; this change adds evidence and a reproducible harness without changing the
application's security behavior.

Evidence was collected from:

- The real Next.js production build on `127.0.0.1:3200`, with execution and account
  services disabled, fake private canaries, and local Chromium probes.
- Actual TypeScript route and server source transpiled with TypeScript and loaded
  in a VM test harness. Supabase, cookies, and Sandbox are explicitly replaced
  with fixtures. The VM is not an isolation boundary for untrusted code.
- The actual initial SQL migration executed in a fresh PGlite PostgreSQL engine,
  with two synthetic users and anonymous/authenticated/service roles.
- Source inspection of the supervisor, snapshot recipe, retention migration,
  client rendering, authentication flow, and CI.
- Fresh audits of both npm lockfiles, including development and optional packages:
  **zero known npm vulnerabilities** at assessment time.

Fifteen probe groups completed without harness failures. This means the probes
ran successfully, not that all security controls passed: the JSON observations
explicitly reproduce open issues S01, S02, S03, S05, and S06. S04 is confirmed by
source inspection and Go's published support policy.

No production requests, cloud quota-consuming jobs, load tests, account attacks,
or attempts to escape a real Sandbox microVM were performed. No live credentials
or learner data were used. Fixtures cannot establish the security of deployed
Supabase policies, OAuth configuration, Vercel forwarding, or the current snapshot.

## Prioritized findings

### S06 — Startup can overwrite a terminal cancellation

**Priority: Medium. OWASP A06/A08/A10. Confirmed deterministic source/SQL probe.**

Location: `app/api/executions/route.ts`, final command/status update, and the
`finish_execution` state machine in the initial database migration.

The start route updates `command_id` and sets `status='running'` using only the job
ID. It does not require the row to still be in a starting/running state. The SQL
completion function correctly prevents terminal-state changes, but this direct
update bypasses that guard.

The probe reserves a real row through `reserve_execution`, interleaves an actual
`finish_execution(..., {status:'cancelled'})` at the detached-command return, and
then resumes the actual start route through a thin PostgreSQL-backed client
adapter. It produces:

```json
{ "status": "running", "result": { "status": "cancelled" } }
```

A concurrent poll/cancel can therefore lose finality while startup completes.
An idempotent retry can obtain an in-progress job ID before the first startup
request finishes. This concerns a caller's own job; cross-user access was not
demonstrated. Potential consequences include inconsistent status, extra active
quota occupancy, and reopening a state that completion logic considers terminal.
No cloud-side timing exploit or forged verified completion was demonstrated.

**Remediation:** perform startup state transitions through a conditional update or
transactional RPC that allows only expected active states. Check whether the
update changed a row; stop a newly created sandbox if the job is already terminal.
Regression-test cancellation and expiry at every startup await point, including
an in-flight completion poll. Preserve the existing terminal-state SQL guard.

### S01 — Body limits are checked after full materialization

**Priority: Medium, deployment-dependent availability exposure. OWASP A06/A10.**

Locations: `app/api/executions/route.ts` and `app/api/drafts/route.ts`.

Both handlers await `request.text()` before measuring bytes. The execution probe
sends a bounded 262,144-byte stream to the real handler with service fixtures.
All 262,144 bytes are consumed before the route returns 413 for its 100,000-byte
limit; no quota admission or Sandbox creation occurs. The draft route uses the
same pattern with an 80,000-byte threshold (source-confirmed, not separately
stream-probed).

An attacker can make the application consume more input memory and processing
than its declared limit before quota admission. Execution must be enabled to
reach its body reader, while draft writes require an authenticated user. Hosting
request limits may cap the exposure; deployed proxy limits, concurrency impact,
and memory exhaustion were not tested. This is not evidence of an actual outage.

**Remediation:** use a bounded stream reader that counts bytes, cancels the stream,
and returns 413 immediately after the limit. Treat `Content-Length` as an early
hint, not the only defense. Verify handling of absent/incorrect lengths and slow
clients, and configure matching hosting request/time limits.

### S02 — Weak guest-session secrets are accepted

**Priority: Medium when misconfigured. OWASP A02/A04/A07. Confirmed fixture probe.**

Location: `lib/server.ts`, `executionConfigured`, `digest`, and `identity`.

The README requests a random secret of at least 32 bytes, but the implementation
checks only that `SESSION_SECRET` is truthy. With the fixture value `x`, execution
is considered configured and a correctly HMAC-signed, attacker-chosen guest UUID
is accepted by the actual identity function.

If a deployment uses a guessable secret, an attacker who guesses it can mint
guest cookies. This weakens guest identity and per-session quota integrity. The
network quota still applies. This does not forge Supabase authentication or prove
account takeover; guest/job identifiers would also be needed to target another
guest's existing resources. The real hosted secret was not inspected or guessed.

**Remediation:** fail closed on short or known placeholder secrets, generate at
least 32 random bytes, validate configuration before enabling execution, and
document rotation invalidating existing guest sessions. Length alone does not
establish entropy. Add negative configuration tests without logging secret values.

### S04 — Snapshot recipe and CI pin an unsupported Go release

**Priority: Medium maintenance exposure. OWASP A03. Source-confirmed.**

Locations: `scripts/sandbox-probe.mjs` pins Go 1.22.12; repository and Windows CI
request Go 1.22. [Go's release policy](https://go.dev/doc/devel/release) supports
only releases until two newer major releases exist; its published history now
includes Go 1.27. The pinned 1.22 line is outside that support window.

An unsupported compiler/runtime does not receive the current line's security
fixes. npm auditing does not cover downloaded toolchains or existing snapshot OS
packages. The recipe's pin is confirmed; the currently deployed snapshot's actual
inventory and exploitable CVEs were not inspected. No Sandbox escape is claimed.

**Remediation:** move CI and the snapshot recipe to a supported patched Go line,
verify artifact checksums, rebuild the snapshot, run the six-language/isolation
integration suite, then update the hosted snapshot ID and retire superseded
snapshots. Updating npm dependencies alone does not update an existing snapshot.

### S03 — No application Content Security Policy

**Priority: Low, defense in depth. OWASP A02. Confirmed local production HTTP.**

Location: `next.config.ts` and the production HTML response.

The local production response has no `Content-Security-Policy` header. Existing
`nosniff`, frame denial, referrer, and permissions headers were present. Reflected
search text and malicious-looking execution output remained inert in Chromium;
an XSS vulnerability was not demonstrated.

**Remediation:** introduce a tailored report-only policy, then enforce it after
testing. Account for the inline theme bootstrap, Next.js scripts, Monaco workers,
blob downloads, and the actual Supabase connection origin. Prefer nonces or hashes
over broad inline-script allowances. Keep frame restrictions. See the
[OWASP CSP guidance](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html).
Hosted edge headers were not inspected and could differ.

### S05 — OAuth provider exceptions bypass controlled fallback

**Priority: Low, availability/error handling. OWASP A10. Confirmed fixture probe.**

Location: `app/auth/callback/route.ts`.

The callback handles a returned `{error}`, but does not catch exceptions from
`auth()` or `exchangeCodeForSession`. A synthetic provider outage causes the
actual route function to reject rather than returning its normal unavailable
redirect. The normal callback ignores attacker-controlled redirect targets.

**Remediation:** catch provider/cookie/network exceptions, return a fixed local
fallback, and log a sanitized correlation event. Do not log OAuth codes or tokens.
Test thrown exceptions as well as returned error objects. Production stack-trace
disclosure was not demonstrated.

## Coverage against all ten categories

| OWASP Top 10:2025                          | Evidence and result                                                                                                                                                                                                            | Remaining work                                                                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A01 Broken Access Control                  | Anonymous drafts rejected; execution ID and owner predicates checked before inspection; real PostgreSQL RLS blocked cross-user reads/writes/deletes, forged ownership, progress insertion, and private execution/quota access. | Validate the migrations and grants in the deployed Supabase instance with two real test accounts; broaden HTTP IDOR cases across GET/DELETE and draft conflicts.        |
| A02 Security Misconfiguration              | Sensitive local paths returned 404; defensive headers present; execution disabled without required services. S02/S03 remain.                                                                                                   | Inspect actual edge headers, allowed OAuth redirects, environment scoping, hosting limits, and production exposure.                                                     |
| A03 Software Supply Chain Failures         | Both complete npm lockfiles audited clean; audit CI and Dependabot configured. S04 remains.                                                                                                                                    | Inventory snapshot OS packages, toolchains, and action dependencies; consider immutable action SHAs and artifact verification.                                          |
| A04 Cryptographic Failures                 | HMAC rejects a forged signature; guest cookies set Secure/HttpOnly/SameSite=Lax; private canaries absent from collected page JavaScript. S02 remains.                                                                          | Verify real key generation/rotation, TLS/HSTS, database transport/storage controls, and cookie behavior behind hosting.                                                 |
| A05 Injection                              | Search and console XSS probes inert; parameterized SQL preserved an injection-shaped code string; submitted commands, filenames, language and expected cases could not replace server metadata.                                | Broaden Markdown/Monaco payload corpus and verify live sandbox/compiler isolation in a trusted environment.                                                             |
| A06 Insecure Design                        | Existing quota/idempotency/concurrency database tests available and run separately. Bounded stream and lifecycle interleaving reproduce S01/S06.                                                                               | Assess sustained abuse, draft retention/capacity, shared-device draft privacy, and provider-level admission.                                                            |
| A07 Authentication Failures                | Server identity uses provider-verified user; forged guest MAC rotates the cookie; missing trusted network identity fails closed; OAuth open redirect probe blocked. S02 remains.                                               | Validate live PKCE/OAuth session expiry, revocation, logout, and login-CSRF with dedicated accounts.                                                                    |
| A08 Software or Data Integrity Failures    | Clients cannot choose grading rules or execution commands; direct progress writes denied; supervisor inspected for root-owned result/oracle separation. S06 remains.                                                           | Validate snapshot provenance and artifact checksums; run real result-tampering and isolation probes.                                                                    |
| A09 Security Logging and Alerting Failures | Start failures log sanitized stage/kind/origin-rejected fields; many other denial/failure handlers return without application-specific security events.                                                                        | Hosted log retention, central alerting, account/IDOR/quota anomaly detection, and incident delivery were not assessed. No assertion that external monitoring is absent. |
| A10 Mishandling of Exceptional Conditions  | Missing services fail closed; oversized input returns 413; existing cancellation-finality SQL checked. S01/S05/S06 remain.                                                                                                     | Inject provider/database failures at every await boundary and verify cleanup, controlled errors, and terminal-state preservation.                                       |

## Reproduction

The assessment run completed with 15 probe groups, 8 existing web unit/database
tests, the production build, web typechecking/formatting, root lint, and full root
verification (62 automation tests, 149 example jobs, 881 exercise jobs, 48 checkpoint
solutions, and uncovered C++/Java builds). These tooling checks do not close the
findings above.

Requirements: Node 22, Python, installed web dependencies, Chromium, and the normal
content prerequisites. Run from `apps/web`:

```bash
npm ci
npx playwright install chromium
npm run security:assess
```

The default command runs only source/service-fixture and local PostgreSQL probes.
For the HTTP/browser probes, first start a dedicated local production server.
In PowerShell, use a separate terminal from `apps/web`:

```powershell
$env:NEXT_DIST_DIR = '.next-test'
$env:EXECUTION_ENABLED = 'false'
$env:NEXT_PUBLIC_SUPABASE_URL = ''
$env:NEXT_PUBLIC_SUPABASE_ANON_KEY = ''
$env:SUPABASE_SERVICE_ROLE_KEY = 'owasp-private-canary-do-not-publish'
$env:SESSION_SECRET = 'owasp-session-canary-do-not-publish'
npm run build
npm run start -- --hostname 127.0.0.1 --port 3200
```

Then, in the assessment terminal:

```bash
npm run security:assess -- --url=http://127.0.0.1:3200
npm test
```

The URL option accepts only explicit loopback HTTP targets. Browser network
requests to other origins are blocked. Execution responses in the XSS probe are
local fixtures. No real Supabase or Sandbox client is imported by the route
fixture loader. The 256 KiB stream is a bounded measurement, not a stress test.

Results are written to ignored `build/owasp-check.json` within `apps/web`. Each
record distinguishes source fixtures, local PostgreSQL, and local production
HTTP/Chromium. Exit status 1 denotes a probe/harness failure; observations can
identify vulnerabilities even when the command exits 0. Compare observations
with the findings above; do not treat the command as a production approval gate.
The result includes the checkout HEAD; uncommitted source changes are not encoded
in that commit ID. Re-run against a clean reviewed checkout for archival evidence.

Stop the dedicated server when finished and do not run this server configuration
alongside another `.next-test` build. Next.js may regenerate `next-env.d.ts` for
that build directory; keep generated-path changes out of unrelated commits.
