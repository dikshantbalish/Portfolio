# Dikshant Balish · Portfolio

> Software Engineer building thoughtful backend systems, AI products, and practical digital experiences.

![FastAPI](https://img.shields.io/badge/FastAPI-0f766e?style=flat-square&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-18252b?style=flat-square&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-e45b3d?style=flat-square&logo=postgresql&logoColor=white)

## About

A personal portfolio for selected work across backend engineering, AI/ML, agentic workflows, and full-stack development. The site includes project details, certifications, resume access, and a contact form that stores messages in PostgreSQL.

## Highlights

- Editorial, responsive portfolio interface
- FastAPI and Jinja2 server-rendered pages
- Project, resume, certification, and contact sections
- PostgreSQL-backed contact form submissions
- PDF links for resume and certifications
- Mobile navigation and subtle motion effects

## Quick Start

### Requirements

- Python 3.11+
- PostgreSQL 14+
- `uv` or `pip`

### Install

```bash
git clone <repository-url>
cd Portfolio
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Configure PostgreSQL

Create a local environment file:

```bash
cp .env.example .env
```

Then set your PostgreSQL connection string in `.env`:

```env
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE
```

The application creates the `contact_messages` table automatically at startup. Each valid submission stores the sender name, email, message, and creation time.

### Run

```bash
uv run uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

Health check: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

## Project Map

```text
main.py              FastAPI application and startup
routes.py            Pages, project data, and contact handling
database.py          PostgreSQL engine and persistence
models.py            SQLAlchemy models
templates/           Jinja2 page templates
static/css/          Visual system
static/js/           Navigation and interaction logic
static/documents/    Resume and certification PDFs
```

## Contact Storage

The contact form validates input before writing to PostgreSQL. If the database is unavailable or `DATABASE_URL` is missing, the form shows an error and does not claim that the message was saved.

## License

See [LICENSE](LICENSE).
