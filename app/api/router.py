# app/api/router.py
from fastapi import APIRouter
from app.services.portfolio_service import compute_portfolio
from app.services.holdings_service import get_holdings
from app.services.pricing_service import get_current_prices, get_price_changes, get_price_changes_percent

api_router = APIRouter()

@api_router.get("/portfolio")
def get_portfolio():
    holdings = get_holdings()
    prices = get_current_prices(holdings)
    changes = get_price_changes(holdings)
    changes_pct = get_price_changes_percent(holdings)
    portfolio = compute_portfolio(holdings, prices, changes, changes_pct)
    return portfolio