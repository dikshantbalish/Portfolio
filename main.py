from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import initialize_database
from routes import router


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"


# =========================================================
# APPLICATION
# =========================================================

app = FastAPI(
    title="Dikshant Balish — Portfolio",
    description=(
        "Portfolio of Dikshant Balish, "
        "Software Engineer and AI Developer."
    ),
    version="1.0.0",
)


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)


# =========================================================
# ROUTES
# =========================================================

app.include_router(router)


@app.on_event("startup")
async def startup_database():
    initialize_database()


# =========================================================
# ROOT HEALTH CHECK
# =========================================================

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "Dikshant Balish Portfolio",
    }