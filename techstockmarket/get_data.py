import yfinance as yf
import os

os.makedirs("data", exist_ok=True)

tickers = ["AAPL", "AMZN", "BABA", "CRM", "META", "GOOG", "INTC", "MSFT", "NVDA", "TSLA",
           "KC=F", "CC=F", "SB=F"]

for t in tickers:
    df = yf.download(t, start="2015-01-01", auto_adjust=False)
    df.columns = df.columns.get_level_values(0)
    df.to_csv(f"data/{t.replace('=F', '')}.csv")
    print("saved", t)