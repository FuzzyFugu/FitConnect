# FitConnect

A lightweight web platform that helps people organise and join fitness meetups and
wellness events — running clubs, yoga classes, group hikes and more.

Built as an 4-week Agile MVP for the FitConnect startup.

## Features (MVP)

- **User registration & login** — secure accounts with hashed passwords
- **Event creation & editing** — organisers publish and manage meetups
- **RSVP system** — join or cancel a place, with capacity limits enforced
- **Dashboard** — a member's upcoming sessions, events they organise, and reminders
- **Notifications** — in-app reminders (pluggable email backend)

## Tech stack

| Layer      | Choice                          |
|------------|---------------------------------|
| Language   | Python 3.12                     |
| Web        | Flask (application-factory)     |
| ORM / DB   | Flask-SQLAlchemy + SQLite       |
| Auth       | Flask-Login                     |
| Forms/CSRF | Flask-WTF / WTForms             |
| Tests      | pytest                          |
| CI         | GitHub Actions                  |

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py                   # http://127.0.0.1:5000
```

## Running the tests

```bash
pytest -q
```

## Project structure

```
app/
  auth/           registration, login, logout
  events/         event CRUD + RSVP
  main/           landing page + dashboard
  notifications/  reminder service (in-app / email)
  models.py       User, Event, RSVP, Notification
  templates/      Jinja2 views
  static/css/     stylesheet
tests/            unit + acceptance (BDD) tests
docs/             Agile artefacts (backlog, sprints, risks, retrospectives)
```

## The team

| Member              | Role                       | Responsibility                                     |
|---------------------|----------------------------|----------------------------------------------------|
| Andrei Andriescu    | Product Owner              | Vision, backlog, user stories, acceptance criteria |
| Ana Gafita          | Scrum Master               | Process, testing framework, CI, Agile artefacts    |
| Maria Bucur         | Backend Developer          | Data model, event/RSVP logic, notifications        |
| Dumitru Galbura     | Login & Frontend Developer | Authentication, templates, UI/UX                   |

See `docs/` for the full Agile documentation trail.
