# FitConnect — Progress Tracking (Burndown / Burnup)

Story points committed vs completed per sprint. Total committed for the MVP: **34 pts**.
Charts (`docs/screenshots/burndown_sprintN.png`) are exported from the Trello
board; the underlying data is kept here so it can be regenerated.

## Points per story
| Story | Points |
|-------|--------|
| Register | 3 |
| Login/logout | 2 |
| Event CRUD | 8 |
| RSVP | 5 |
| Reminders | 3 |
| Dashboard | 5 |
| Setup (Sprint 0) | 5 |
| Testing/CI/docs | 3 |

## Sprint burndown data (ideal vs actual remaining points)

### Sprint 1 (committed 10 pts)
| Day | Ideal remaining | Actual remaining |
|-----|-----------------|------------------|
| 1   | 10 | 10 |
| 3   | 7  | 9  |
| 5   | 5  | 6  |
| 7   | 3  | 4  |
| 10  | 0  | 0  |

### Sprint 2 (committed 16 pts)
| Day | Ideal remaining | Actual remaining |
|-----|-----------------|------------------|
| 1   | 16 | 16 |
| 3   | 12 | 15 |
| 5   | 9  | 11 |
| 7   | 5  | 6  |
| 10  | 0  | 2  |   ← 2 pts (dashboard polish) carried to Sprint 3

### Sprint 3 (committed 8 pts + 2 carried = 10)
| Day | Ideal remaining | Actual remaining |
|-----|-----------------|------------------|
| 1   | 10 | 10 |
| 3   | 7  | 8  |
| 5   | 5  | 5  |
| 7   | 2  | 2  |
| 10  | 0  | 0  |

## Velocity
Sprint 1: 10 · Sprint 2: 14 · Sprint 3: 10 → average **~11 pts/sprint**, stable
and sufficient to clear the 34-point MVP within the 4-week window.
