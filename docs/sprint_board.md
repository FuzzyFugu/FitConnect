# FitConnect — Sprint Boards

Framework: **Scrum** (1-week sprints, 3 sprints across the 4-week engagement).
Board columns: `Backlog → To Do → In Progress → In Review → Done`.
(Exported snapshots of the live Trello board are stored in `docs/screenshots/`.)

---

## Sprint 0 — Setup (Week 1)
**Goal:** repository, architecture and definition-of-done agreed.

| Item | Owner | Status |
|------|-------|--------|
| Project scaffold, README, backlog | Andrei (PO) | Done |
| App factory, config, data model | Marina (BE) | Done |
| Agree Definition of Done & branching model | Ana (SM) | Done |

## Sprint 1 — Accounts (Weeks 2)
**Goal:** members can register, log in and reach a dashboard.

| Item | Owner | Status |
|------|-------|--------|
| Registration + login + logout | Dumitru (FE) | Done |
| Test framework + auth unit tests | Ana (SM) | Done |

## Sprint 2 — Events & RSVP (Weeks 3)
**Goal:** the core loop — create an event, RSVP, get a reminder.

| Item | Owner | Status |
|------|-------|--------|
| Event CRUD + RSVP + notifications | Marina (BE) | Done |
| Templates, dashboard UI, styling | Dumitru (FE) | Done |

## Sprint 3 — Hardening & sign-off (Weeks 4)
**Goal:** acceptance criteria proven; risks retired; CI green.

| Item | Owner | Status |
|------|-------|--------|
| BDD acceptance tests + risk board | Andrei (PO) | Done |
| CI pipeline + Agile docs + retro | Ana (SM) | Done |

## Week 4 — Buffer / demo prep
Reserved for exploratory testing, bug-fixes and stakeholder demo.

### Definition of Done
- Code reviewed via pull request by at least one other developer.
- Unit and/or acceptance tests written and passing in CI.
- Code commented; no linter errors; merged to `main`.
