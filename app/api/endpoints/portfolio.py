from fastapi import APIRouter
from app.services.holdings_service import get_holdings
from app.services.pricing_service import (
    get_current_prices,
    get_price_changes,
    get_price_changes_percent
)
from app.services.portfolio_service import compute_portfolio

router = APIRouter()

@router.get("/")
def get_portfolio():
    holdings = get_holdings()
    prices = get_current_prices(holdings)
    changes = get_price_changes(holdings)
    changes_pct = get_price_changes_percent(holdings)

    return compute_portfolio(
        holdings,
        prices,
        changes,
        changes_pct
    )
