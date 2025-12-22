from rich.table import Table


def portfolio_table(portfolio: dict) -> Table:

    # Title
    table = Table(title="Portfolio Standings")

    # Columns
    table.add_column("Ticker", style="bold", no_wrap=True)
    table.add_column("Shares", justify="right")
    table.add_column("Price ($)", justify="right")
    table.add_column("Value ($)", justify="right")
    table.add_column("Change ($)", justify="right")
    table.add_column("Change (%)", justify="right")

    # Rows
    rows = portfolio.get("rows", [])

    for row in rows:
        ticker = row.get("ticker", "")
        shares = row.get("shares", 0)
        price = row.get("price", 0.0)
        value = row.get("value", 0.0)
        change = row.get("change", 0.0)
        change_pct = row.get("change_percent", 0.0)

        color = "green" if change >= 0 else "red"
        symbol = "▲" if change >= 0 else "▼"

        table.add_row(
            str(ticker),
            str(shares),
            f"{price:.2f}",
            f"{value:.2f}",
            f"[{color}]{symbol} ${abs(change):.2f}",
            f"[{color}]{symbol} %{abs(change_pct):.2f}",
        )

    # Totals at bottom
    table.add_section()

    total_value = portfolio.get("total_value", 0.0)
    total_change = portfolio.get("total_change", 0.0)
    total_change_pct = portfolio.get("total_change_percent", 0.0)

    total_color = "green" if total_change >= 0 else "red"
    total_symbol = "▲" if total_change >= 0 else "▼"

    table.add_row(
        "[bold]TOTAL[/]",
        "",
        "",
        f"[bold]{total_value:,.2f}[/]",
        f"[bold][{total_color}]{total_symbol} ${abs(total_change):,.2f}[/]",
        f"[bold][{total_color}]{total_symbol} %{abs(total_change_pct):,.2f}[/]",
    )

    return table