from contextlib import asynccontextmanager
from app.services.history_service import init_db

@asynccontextmanager
async def lifespan(app):
    init_db()
    # Startup logic
    print("HexFolio starting up")

    yield

    # Shutdown logic
    print("HexFolio shutting down")
