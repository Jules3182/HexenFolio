from fastapi import APIRouter
from app.api.endpoints import portfolio, ticker, history, holdings, settings

api_router = APIRouter()

api_router.include_router(
    portfolio.router,
    prefix="/portfolio",
    tags=["portfolio"]
)

api_router.include_router(
    ticker.router,
    prefix="/ticker",
    tags=["ticker"]
)

api_router.include_router(
    history.router,
    prefix="/history",
    tags=["history"]
)

api_router.include_router(
    history.router,
    prefix="/holdings",
    tags=["holdings"]
)

api_router.include_router(
    settings.router,
    prefix="/settings",
    tags=["settings"]
)