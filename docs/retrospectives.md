# FitConnect — Sprint Retrospectives

Facilitated by Ana (Scrum Master). Format: **What went well / What didn't /
Actions**. Captured live at the end of each sprint.

---

## Sprint 1 Retrospective (end Week 1)
**Went well**
- Auth delivered on schedule; TDD caught a duplicate-email bug before review.
- Definition of Done gave clear merge criteria and removed "is this finished?" debate.

**Didn't go well**
- Two developers touched `models.py` in the same day → a small merge conflict.
- Estimates for form validation were optimistic.

**Actions**
- Backend owns `models.py`; others request changes via PR comment. *(→ R3, R4)*
- Add a 20% buffer to first estimate of any new UI form.

---

## Sprint 2 Retrospective (end Week 2)
**Went well**
- Core loop (create → RSVP → reminder) demoed successfully at sprint review.
- Notification service abstraction paid off — email stayed a stub, no rework.

**Didn't go well**
- Capacity edge-case (full event) initially slipped through manual testing.
- Frontend waited on backend RSVP endpoints early in the sprint.

**Actions**
- Add an explicit capacity unit test. *(done: `test_capacity_is_enforced`)*
- Backend to expose endpoint stubs first so frontend can integrate in parallel.

---

## Sprint 3 Retrospective (end Week 3)
**Went well**
- BDD acceptance tests mapped 1:1 to stories, making sign-off with the PO fast.
- CI on GitHub Actions stopped a regression reaching `main`.

**Didn't go well**
- Documentation nearly lagged behind code in the busy mid-sprint period.

**Actions**
- "Docs are part of Done" — update `docs/` in the same PR as the feature.
- Reserve Week 4 buffer for exploratory testing and demo polish.

## Exploratory testing findings (Week 4, session-based)
- Charter: "explore RSVP under odd navigation/back-button use."
  - Finding: double-submitting RSVP handled correctly (unique constraint). ✔
- Charter: "explore event form with invalid dates."
  - Finding: past dates accepted at DB level → logged as backlog item US-11.
- Charter: "explore mobile layout at 360px."
  - Finding: dashboard grid collapses cleanly to one column. ✔
