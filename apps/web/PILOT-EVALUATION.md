# Python guided pilot: observation protocol

## Purpose and setup

Invite 3–5 adults who are new to programming. The project owner recruits the
participants; implementation does not contact anyone or collect analytics.
Allow 25–35 minutes per session. Explain that the website is being evaluated,
not the participant. They may stop at any time. No recording is necessary.

Use the Python Types and Input/Output guided lesson. Include at least one mobile
session and both color themes across the sessions. Use a fresh browser profile
for each participant. Sign-in is optional; never ask for passwords or inspect
personal accounts. If quota is unavailable, use the labelled reference output
and note this limitation rather than presenting it as a real run.

Ask the participant to think aloud. Avoid explaining where to click before they
try. Count any directional help as navigation assistance. Help if they become
stuck, recording which step needed intervention. Record observations under
participant codes P1–P5, without names, contact details, code, input values, or
credentials. Keep notes locally with the owner and delete them after synthesis.

## Tasks

1. Find and start the guided lesson from the curriculum.
2. Read the short explanation and explain what `input()` returns.
3. Predict the Adult line for age 17; submit an answer and interpret the feedback.
4. Open the example and load prepared inputs. Execute if quota is available;
   otherwise distinguish the reference output from an actual execution.
5. Change the age and GPA, predict the new output, and compare it when possible.
6. Open each exercise. Ask where to find a hint and what a failed case means.
   Solving both from scratch is optional within the observation time box.
7. Answer the three review questions without hints from the facilitator.
8. Reload and continue. Find the exercise history and explain the difference
   between reviewed steps, local progress, and server-verified history.

For the learning signal, record the first submitted answer to each final question
before its explanation is revealed. Later retries are useful practice but do not
replace that first-attempt measure. A completed route means visiting all six
steps and attempting all three final questions; it does not require approving
both coding exercises or marking all steps reviewed.

## Observation sheet

| Participant code | Device/theme | Navigation help needed and step | First review score / 3 | Route completed | Main confusion | Quota unavailable |
| ---------------- | ------------ | ------------------------------- | ---------------------- | --------------- | -------------- | ----------------- |
| P1               |              |                                 |                        |                 |                |                   |
| P2               |              |                                 |                        |                 |                |                   |
| P3               |              |                                 |                        |                 |                |                   |
| P4               |              |                                 |                        |                 |                |                   |
| P5               |              |                                 |                        |                 |                |                   |

Ask afterward: What did `input()` return? Why convert it? Why check the count
before an average? What would you do after a failed case? What does “verified” mean?
Summarize misunderstandings without quoting identifying information.

## Expansion decision

Resolve repeated navigation or feedback difficulties first. The initial signal
is at least 80% of participants completing the route without navigation help
and answering at least two of the three review questions correctly on their first
attempt. Round the required number up (3/3, 4/4, or 4/5). Report denominators and
quota-related limitations explicitly. This small sample guides iteration and is
not statistical evidence of educational efficacy. Plan expansion only after
reviewing the observed issues with the owner.

## Content maintenance

The journey is authored in `content/guided-lessons.json`. Its pedagogical version
is separate from the Git content SHA. Increment that version when questions,
step meaning, or answer interpretation changes. The old journey remains stored
under its previous version; the new version starts fresh without deleting drafts.
UI-only commits do not reset journey answers. Example fragments are extracted
from canonical source and feedback references existing activity/case names.

The authenticated progress endpoint is read-only and uses the user's Supabase
client with RLS. No new Supabase tables or migrations are required. Journey answers
and local activity history remain in IndexedDB and are never uploaded by draft
synchronization. Reference output and questions make no execution requests.
