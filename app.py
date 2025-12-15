import yaml
import yfinance as yf
import time

# Rich stuff for live updates and console
from rich.live import Live
from rich.console import Console

# Utils split into other file for future use
from holdings_utils import add_ticker, remove_ticker, set_ticker_value

# Terminal management stuff moved to other file
import tui

# Loads up user config on start
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Gets listed tickers from holdings.yaml
def load_holdings():
    with open("holdings.yaml", "r") as f:
        data = yaml.safe_load(f)
        return data["tickers"]

# Get opening prices for each ticker
# (I need to cache this somewhere and only call during market hours if data is old)
def get_opening_prices(holdings: dict):
    opening_prices = {}

    for ticker in holdings.keys():
        hist = yf.Ticker(ticker).history(period="1d", interval="1m")

        opening_prices[ticker] = (
            float(hist.iloc[0]["Open"]) if not hist.empty else None
        )

    return opening_prices

# Pulls stock price for each ticker
def get_current_prices(holdings: dict):
    tickers = list(holdings.keys())

    # Actually gets the data from yfinance
    data = yf.download(
        tickers,
        period="1d",
        interval="1m",
        progress=False,
        auto_adjust=True
    )

    # Picks out the "close" price
    close = data["Close"].iloc[-1]

    # Fix for dict's being passed into functions
    if hasattr(close, "to_dict"):
        return close.to_dict()

    return {tickers[0]: float(close)}

# Calculates the daily change in price
def get_price_changes(tickers):
    # Getting the open prices and current prices to compare
    opens = get_opening_prices(tickers)
    currents = get_current_prices(tickers)

    # List for changes in price
    changes = {}

    # Loop for each ticker calculating change from opening to current price
    for ticker in tickers:
        o = opens.get(ticker)
        c = currents.get(ticker)

        # Case for no change
        # (Doesn't have any use really yet but I will fix that)
        if o is None or c is None:
            changes[ticker] = None
        else:
            changes[ticker] = (c - o)

    return changes
    
# Main Run Loop
def main():
    # Checking if TUI is disabled in config
    if not config["tui_on"]:
        print("Tui Not Active")
        return

    # Setting up variables for easy passing in
    console = Console()
    holdings = load_holdings()

    try:
        # Live loop for constantly refreshing TUI tables
        with Live(
            tui.portfolio_table(holdings, {}, {}),
            console=console,
            refresh_per_second=2,
        ) as live:

            while True:
                # Pulling most recent data to pass in
                current_prices = get_current_prices(holdings)
                price_changes = get_price_changes(holdings)

                # Refreshing the table with fresh data, realistically I should cache the holdings but I like this for now
                live.update(
                    tui.portfolio_table(
                        holdings,
                        current_prices,
                        price_changes
                    )
                )

                # Updates at user configured speed
                time.sleep(config["update_time"])

    # Exit case and little "sign off" print
    except KeyboardInterrupt:
        console.print("\n[bold red]Quitting HexFolio TUI[/]")


if __name__ == "__main__":
    main()