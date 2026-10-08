# FastAPI Study

A hands-on repository for learning and practicing FastAPI. It contains lesson
examples and a small API project that grows alongside the course.

## Course roadmap

The course has eight lessons. The repository currently contains the Lesson 1
routing example; the roadmap below describes the planned hands-on work, AI
assistance, and the corresponding LMS project milestones.

| Lesson | Content | Hands-on (Tay) | AI | LMS project (Assignment 5) |
| --- | --- | --- | --- | --- |
| 1 | Routing, path/query/body parameters, and status codes | Build the basic endpoints and sample data | Set up the in-memory course API skeleton | In-memory course API |
| 2 | Pydantic, validation, and `response_model` | Create simple schemas with `Field` | Add more complex validators | Define `Course`, `Lesson`, and `User` schemas |
| 3 | SQLAlchemy, SQLite, and `Depends` | Complete CRUD for one model | Add CRUD for the remaining tables | Store courses in SQLite |
| 4 | Project structure, `APIRouter`, error handling, and `.env` | Split out the first router | Split out the remaining routers | Refactor `proj_code` |
| 5 | Password hashing, JWT, current user, and roles | Implement registration, login, and token creation/verification | Add authorization across endpoints | Login with student, teacher, and admin roles |
| 6 | Table relationships, pagination, and filtering | Implement one-to-many relationships | Add many-to-many relationships and complex queries | Add chapters, lessons, and enrollment |
| 7 | pytest, `TestClient`, and dependency overrides | Write the first test and a database fixture | Test the remaining endpoints | Build an LMS test suite |
| 8 | PostgreSQL, Alembic, and Docker | Understand the configuration and run the commands | Create a Dockerfile, Compose setup, and migrations | Move the LMS to PostgreSQL and Docker |

The LMS project is developed incrementally across the lessons, progressing
from an in-memory API to a tested, database-backed application.

## Repository contents

- [`study_code/bai1_routing/vi_du/main.py`](study_code/bai1_routing/vi_du/main.py)
  is the Lesson 1 routing example. It demonstrates routes for listing, filtering,
  creating, updating, and deleting courses, along with path parameters,
  enumerations, request validation, and HTTP errors. Its sample data is held in
  memory.
- [`proj_code/main.py`](proj_code/main.py) is a coffee-store API practice
  project. It includes menu endpoints, keyword and price filters, item sizes,
  and in-memory CRUD operations.
- [`pyproject.toml`](pyproject.toml) defines the project and its dependencies;
  [`uv.lock`](uv.lock) locks dependency versions.

## Getting started

Requirements: Python 3.12 or later and [uv](https://docs.astral.sh/uv/).

From the repository root, install the dependencies:

```bash
uv sync
```

Start the coffee-store practice API:

```bash
uv run fastapi dev proj_code/main.py
```

Or start the Lesson 1 course example:

```bash
uv run fastapi dev study_code/bai1_routing/vi_du/main.py
```

FastAPI's interactive API documentation is available at
[`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) while the server is
running.

## Notes

These examples are for study and practice. They use in-memory data, so changes
made through the API are not persisted when the server restarts.
