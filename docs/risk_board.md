# FitConnect — Agile Risk Board

Reviewed at every sprint planning and retrospective. Probability/Impact scored
Low/Med/High. Owner is accountable for the mitigation, not necessarily the fix.

| ID | Risk | Prob | Impact | Mitigation (Agile response) | Owner | Status |
|----|------|------|--------|------------------------------|-------|--------|
| R1 | Scope creep pushes MVP past 8 weeks | High | High | Strict MoSCoW; optional features stay in backlog until Musts are Done | Andrei (PO) | Monitored |
| R2 | Tight budget limits paid services (email, hosting) | Med | Med | Notifications abstracted behind a service; email is a pluggable stub for MVP | Marina (BE) | Mitigated |
| R3 | Small team — key-person dependency | Med | High | Pair reviews on every PR; shared Definition of Done; docs kept current | Ana (SM) | Mitigated |
| R4 | Data-model churn breaks features late | Med | Med | Model agreed in Sprint 0; changes require a migration note + test update | Marina (BE) | Monitored |
| R5 | Security: weak auth / credential leakage | Low | High | Hashed passwords, CSRF via Flask-WTF, session auth via Flask-Login | Dumitru (FE) | Mitigated |
| R6 | Under-testing due to time pressure | Med | High | TDD on core logic; CI blocks merges on failing tests | Ana (SM) | Mitigated |
| R7 | Poor UX loses early adopters | Med | Med | Simple, responsive, single-accent design; usability check each sprint review | Dumitru (FE) | Monitored |

## Agile risk approach
Risks are treated as living backlog items, not a one-off register. Each is
revisited during the retrospective; a risk that materialises is converted into a
spike or bug ticket and pulled into the next sprint.
