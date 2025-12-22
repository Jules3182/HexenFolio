# app/api/endpoints/portfolio.py
from fastapi import APIRouter
from app.services.holdings_service import get_holdings
from app.services.portfolio_service import compute_portfolio

router = APIRouter()

@router.get("/portfolio")
def portfolio():
    holdings = get_holdings()
    return compute_portfolio(holdings)