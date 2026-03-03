# HRMS (Django)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Database

- **PostgreSQL** (default): Create database `hrms`, set `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` if needed, then:
  ```bash
  python manage.py migrate
  ```
- **SQLite** (local dev): `USE_SQLITE=1 python manage.py migrate`

## Run

```bash
python manage.py runserver
```
Use `USE_SQLITE=1` if not using PostgreSQL.
