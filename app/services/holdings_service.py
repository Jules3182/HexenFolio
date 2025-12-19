from app.core.config import HOLDINGS_DATA, BASE_DIR
from pathlib import Path
import yaml

HOLDINGS_PATH = BASE_DIR / "holdings.yaml"

# Internal function for saving the input to holdings YAML
def _save():
    with open(HOLDINGS_PATH, "w") as f:
        yaml.safe_dump(HOLDINGS_DATA, f, sort_keys=True)

# Service for cleanly returning holdings from one place
def get_holdings():
    return HOLDINGS_DATA["tickers"]

# Service for adding a ticker to your portfolio
def add_ticker(symbol: str, shares: float) -> None:
    symbol = symbol.upper()

    tickers = HOLDINGS_DATA["tickers"]

    # Catches duplicates
    if symbol in tickers:
        raise ValueError(f"Ticker '{symbol}' already exists. Would you like to add shares to it instead?")

    tickers[symbol] = {"shares": float(shares)}
    _save()

# Service for removing a ticker from your holdings
def remove_ticker(symbol: str) -> None:
    symbol = symbol.upper()

    tickers = HOLDINGS_DATA["tickers"]

    # Catches trying to remove a ticker that you don't have
    if symbol not in tickers:
        raise ValueError(f"Ticker '{symbol}' does not exist in your holdings")

    del tickers[symbol]
    _save()

# Service for adjusting the number of shares (will be expanded apon later for use in a proper interface i.e. add X, subtract Y, etc)
def set_ticker_shares(symbol: str, shares: float) -> None:
    symbol = symbol.upper()
    tickers = HOLDINGS_DATA["tickers"]

    # Catches attempting to change the number of stocks when not in holdings
    if symbol not in tickers:
        raise ValueError(f"Ticker '{symbol}' does not exist in your holdings. Would you like to add it to your holdings?")

    tickers[symbol]["shares"] = float(shares)
    _save()