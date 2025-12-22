from app.services.pricing_service import (
    get_current_prices,
    get_opening_prices,
    get_price_changes,
    get_price_changes_percent
)

def compute_portfolio(
    holdings: dict,
    prices: dict,
    changes: dict,
    changes_percent: dict,
):
    rows = []
    total_value = 0.0
    total_change = 0.0

    for ticker, shares in holdings.items():
        price = prices.get(ticker)
        delta = changes.get(ticker)
        delta_pct = changes_percent.get(ticker)

        if price is None or delta is None:
            continue

        value = price * shares
        change_value = delta * shares

        total_value += value
        total_change += change_value

        rows.append({
            "ticker": ticker,
            "shares": shares,
            "price": price,
            "value": value,
            "change": change_value,
            "change_percent": delta_pct,
        })

    total_change_percent = (
        (total_change / (total_value - total_change)) * 100
        if total_value != total_change
        else 0.0
    )

    return {
        "rows": rows,
        "total_value": total_value,
        "total_change": total_change,
        "total_change_percent": total_change_percent,
    }