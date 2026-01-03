from fastapi import APIRouter
from app.services.holdings_service import get_holdings
from app.services.pricing_service import (
    get_current_prices,
    get_price_changes,
    get_price_changes_percent
)

router = APIRouter()

@router.get("/")
def get_ticker():
    holdings = get_holdings()
    prices = get_current_prices(holdings)
    changes = get_price_changes(holdings)
    changes_pct = get_price_changes_percent(holdings)

    lines = []

    for ticker, shares in holdings.items():
        price = prices[ticker]
        change = changes[ticker]
        pct = changes_pct[ticker]

        if price is None:
            continue

        safe_change = change if change is not None else 0.0
        safe_percent = pct if pct is not None else 0.0

        trend = (
            "unknown" if change is None
            else "up" if change >= 0
            else "down"
        )

        symbol = "▲" if trend == "up" else "▼"

        text = (
            f"{ticker} "
            f"{price:.2f} "
            f"{symbol} "
            f"{abs(safe_change):.2f} "
            f"({abs(safe_percent):.2f}%)"
        )

        # Puts together the line to be displayed in a scroller
        lines.append({
            "symbol": symbol,
            "price": price,
            "change": change,
            "change_percent": pct,
            "trend": trend,
            "text": text
        })

    return {"lines": lines}
