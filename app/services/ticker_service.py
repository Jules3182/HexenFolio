# Will be for returning ticker data as json (I have a cool idea for this to interact with ESP32/Arduinos to make one of those ticker scroller displays)

def trend_from_value(value: float) -> str:
    return "up" if value >= 0 else "down"

def get_ticker_lines():
    holdings = get_holdings()
    prices = get_current_prices(holdings)
    deltas = get_price_changes_percent(holdings)

    totals = compute_portfolio_totals(holdings, prices, deltas)

    lines = []

    lines.append({
        "text": (
            f"HEXFOLIO | TOTAL ${totals['total_value']:,.2f} "
            f"{totals['total_change_percent']:+.2f}%"
        ),
        "trend": trend_from_value(totals["total_change_percent"])
    })

    for ticker in holdings:
        price = prices.get(ticker)
        delta = deltas.get(ticker)

        if price is None or delta is None:
            continue

        lines.append({
            "text": f"{ticker} ${price:.2f} {delta:+.2f}%",
            "trend": trend_from_value(delta)
        })

    return {
        "lines": lines,
        "updated_at": datetime.utcnow().isoformat()
    }
