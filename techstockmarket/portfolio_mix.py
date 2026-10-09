import numpy as np
import pandas as pd
from analysis import load_prices

tech = ["AAPL","AMZN","BABA","CRM","META","GOOG","INTC","MSFT","NVDA","TSLA"]
comm = ["CC","KC","SB"]

prices = load_prices("data")
rets = np.log(prices / prices.shift(1)).dropna()  # only days where all 13 traded
mu = rets.mean() * 252
cov = rets.cov() * 252

rows = []
for share in np.arange(0, 1.01, 0.1):
       w = pd.Series(0.0, index=rets.columns)
       w[comm] = (1 - share) / len(comm)
       w[tech] = share / len(tech)
       ret = float(w @ mu)
       vol = float(np.sqrt(w @ cov @ w))
       rows.append({"tech_share_pct": round(share * 100),
                    "ann_return": ret,
                    "ann_volatility": vol,
                    "return_per_risk": ret / vol})

print(pd.DataFrame(rows).round(3).to_string(index=False))