# Practice Server

A basic FastAPI server with CRUD endpoints for items, stored in PostgreSQL via SQLAlchemy.

## Setup

```bash
cd "Practice Server"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Database setup (pick one)

**Option A: Homebrew**
```bash
brew install postgresql@16
brew services start postgresql@16
createdb practice_db
```
Homebrew sets up your Mac username as the database user with no password, so in `.env` use:
`DATABASE_URL=postgresql+psycopg://<your-mac-username>@localhost:5432/practice_db`

**Option B: Docker**
```bash
docker compose up -d
```
The default `.env` values already match `docker-compose.yml`.

Then copy the example env file if you haven't already:
```bash
cp .env.example .env
```

Tables are created automatically when the server starts.

## Run

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive Swagger UI.

## Endpoints

| Method | Path              | Description        |
|--------|-------------------|--------------------|
| GET    | /                 | Hello message      |
| GET    | /api/v1/health           | Health check       |
| GET    | /api/v1/items            | List all items     |
| GET    | /api/v1/items/{id}       | Get one item       |
| POST   | /api/v1/items            | Create an item     |
| PUT    | /api/v1/items/{id}       | Update an item     |
| DELETE | /api/v1/items/{id}       | Delete an item     |

## Project structure

```
app/
├── main.py              # Creates the FastAPI app, includes the main router
├── core/config.py       # Settings (app name, API prefix)
├── middleware/        # Runs on every request (logging, CORS)
├── api/
│   ├── router.py        # Combines all route files into one APIRouter
│   └── routes/          # One file per feature (items.py, health.py)
├── schemas/             # Pydantic request/response shapes
├── models/              # SQLAlchemy table models
├── services/            # Business logic, called by routes
└── db/database.py       # Engine, session, Base, get_db dependency
```

Request flow: route → service → db, with schemas validating input and output.
