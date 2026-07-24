# FitConnect — Product Backlog & User Stories

Owner: Andrei Andriescu (Product Owner)
Format: `As a <role> I want <goal> so that <benefit>` with acceptance criteria.
Priority uses MoSCoW (Must / Should / Could / Won't-for-now).

---

### Register an account  *(Must)*
As a new visitor I want to register so that I can create and join events.
**Acceptance criteria**
- Given valid username, email and matching passwords, an account is created.
- Duplicate email or username is rejected with a clear message.
- On success I am logged in and taken to my dashboard.
Covered by: `test_auth.py`, `test_acceptance.py::test_new_member_can_sign_up...`

### Log in and out  *(Must)*
As a returning member I want to log in and out so that my data stays private.
**Acceptance criteria**
- Correct credentials log me in; wrong credentials show an error.
- Logging out ends my session.
Covered by: `test_auth.py`

### Create and edit an event  *(Must)*
As an organiser I want to create and edit events so that people can find them.
**Acceptance criteria**
- I can set title, description, location, category, date/time and capacity.
- Only the organiser of an event may edit it.
Covered by: `test_events.py`

### RSVP to an event  *(Must)*
As a member I want to RSVP (and cancel) so that my place is saved.
**Acceptance criteria**
- I can join an event that isn't full; I can cancel my place.
- A member cannot exceed an event's capacity.
- I cannot RSVP twice to the same event.
Covered by: `test_rsvp.py`, `test_acceptance.py`

### Reminders  *(Should)*
As a member I want a reminder when I join so that I don't forget to attend.
**Acceptance criteria**
- Joining or cancelling creates an in-app notification.
- Notifications appear on the dashboard, newest first.
Covered by: `test_acceptance.py::test_member_receives_reminder...`

### Dashboard of upcoming sessions  *(Must)*
As a member I want a dashboard so that I can see my upcoming sessions at a glance.
**Acceptance criteria**
- Shows sessions I'm attending and events I organise (upcoming only).
Covered by: `test_acceptance.py`

### Backlog (not in MVP scope) — *(Could / Won't-for-now)*
- Email reminders via a real provider (Could)
- Event search & filter by category/location (Could)
- Organiser messaging to attendees (Won't-for-now)
- Social sharing links (Won't-for-now)
