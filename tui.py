import time
import os

from rich import print
from rich.table import Table
from rich.console import Console
from rich.live import Live

from holdings_utils import load_holdings as hu

console = Console()

def portfolio_table(holdings: dict, prices, change) -> Table:
    # Set up for the portfolio stats displayed in the terminal with rich
    table = Table(title="Portfolio Standings")

    table.add_column("Ticker", style="bold", no_wrap=True)
    table.add_column("Shares", no_wrap=True)
    table.add_column("Price ($)", no_wrap=True)
    table.add_column("Value ($)", no_wrap=True)
    table.add_column("Change ($)", no_wrap=True)
    # Will add columns for % change and % of portfolio later
    # User config for what columns are shown?

    # Sets total variables
    total = 0
    total_change = 0.0

    # Sets up breakdown list for use in print loop
    breakdown = []

    # Loops through each ticker pulling price and number of shares
    for ticker, shares in holdings.items():
        price = prices.get(ticker)
        delta = change.get(ticker)

        # Skip invalid/missing prices
        if price is None:
            continue

        # Handles the math
        value = price * shares
        total += value
        total_change += delta

        # Messing aroind with visual Up/Down stuff with rich
        color = "green" if (delta >= 0) else "red"
        symbol = "▲" if (delta >= 0) else "▼"

        # Looping through tickers, pulling the data we need, and putting it in the right spots
        table.add_row(
            str(ticker),
            str(shares),
            f"{float(price):.2f}",
            f"{float(value):.2f}",
            f"[{color}]{symbol} ${abs(float(delta)):.2f}"
        )
    
    # Stylimg for bottom rown, I will likely split this off into a new function later
    color = "green" if (total_change >= 0) else "red"
    symbol = "▲" if (total_change >= 0) else "▼"

    # Adds a row at the bottom for the total value and price change over the day
    table.add_section()
    table.add_row(
        "[bold]TOTAL[/]",
        "",
        "",
        f"[bold]{total:,.2f}[/]",
        f"[bold][{color}]{symbol} ${abs(total_change):,.2f}[/]"
    )

    return table