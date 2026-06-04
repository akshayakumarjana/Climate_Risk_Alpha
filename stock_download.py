import pandas as pd
import yfinance as yf

tickers = ["XOM", "CVX", "AIG", "TRV", "NEE", "DE"]

# ----------------------------
# Download stocks
# ----------------------------

for ticker in tickers:

    data = yf.download(
        ticker,
        start="2015-01-01",
        end="2025-12-31",
        auto_adjust=False
    )

    # Flatten MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()

    data.to_csv(
        f"data/stocks/{ticker}.csv",
        index=False
    )

    print(f"{ticker} downloaded")

# ----------------------------
# Download S&P500
# ----------------------------

sp500 = yf.download(
    "^GSPC",
    start="2015-01-01",
    end="2025-12-31",
    auto_adjust=False
)

if isinstance(sp500.columns, pd.MultiIndex):
    sp500.columns = sp500.columns.get_level_values(0)

sp500 = sp500.reset_index()

sp500.to_csv(
    "data/stocks/SP500.csv",
    index=False
)

print("SP500 downloaded")