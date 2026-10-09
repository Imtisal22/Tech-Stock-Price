import pandas as pd
import numpy as np
from pathlib import Path

def load_prices(folder="data"):
    closes = {}
    for f in Path(folder).glob("*.csv"):
        df = pd.read_csv(f, parse_dates=["Date"], index_col="Date")
        closes[f.stem.upper()] = df["Close"]
    return pd.DataFrame(closes).sort_index()

def summarize(prices):
    rets = np.log(prices / prices.shift(1)).dropna(how="all")
    out = pd.DataFrame({
        "last_close": prices.ffill().iloc[-1],
        "pct_gain": (prices.apply(lambda s: s.dropna().iloc[-1] / s.dropna().iloc[0]) - 1) * 100,
        "ann_return": rets.mean() * 252,
        "ann_volatility": rets.std() * np.sqrt(252),
    })
    out["return_per_risk"] = out["ann_return"] / out["ann_volatility"]
    return out.sort_values("pct_gain", ascending=False)

if __name__ == "__main__":
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", None)
    prices = load_prices("data")
    print(summarize(prices).round(2))
    print()
    print(prices.pct_change(fill_method=None).corr().round(2))