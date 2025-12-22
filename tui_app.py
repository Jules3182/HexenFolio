# tui_app.py
import time
from rich.live import Live
from rich.console import Console
from app.core.config import CONFIG
from app.services.holdings_service import get_holdings
from app.services.pricing_service import (
    get_current_prices,
    get_price_changes,
    get_price_changes_percent,
)
from app.services.portfolio_service import compute_portfolio
from tui.tables import portfolio_table

def run_tui():
    if not CONFIG["tui_on"]:
        print("TUI not active")
        return

    console = Console()
    holdings = get_holdings()

    with Live(
        portfolio_table({
            "rows": [],
            "total_value": 0,
            "total_change": 0,
            "total_change_percentage": 0
        }),
        console=console,
        refresh_per_second=2
        ) as live:
        try:
            while True:
                prices = get_current_prices(holdings)
                changes = get_price_changes(holdings)
                changes_pct = get_price_changes_percent(holdings)

                portfolio = compute_portfolio(
                    holdings,
                    prices,
                    changes,
                    changes_pct,
                )

                live.update(portfolio_table(portfolio))
                time.sleep(CONFIG["update_time"])

        except KeyboardInterrupt:
            console.print("\n[bold red]Quitting HexFolio TUI[/]")

if __name__ == "__main__":
    run_tui()