from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    # 🔹 Startup logic
    print("🚀 HexFolio starting up")

    yield

    # 🔹 Shutdown logic
    print("🛑 HexFolio shutting down")
