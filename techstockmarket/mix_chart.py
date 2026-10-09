import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analysis import load_prices

tech = ["AAPL","AMZN","BABA","CRM","META","GOOG","INTC","MSFT","NVDA","TSLA"]
comm = ["CC","KC","SB"]

prices = load_prices("data")
rets = np.log(prices / prices.shift(1)).dropna()
mu, cov = rets.mean() * 252, rets.cov() * 252

shares = np.arange(0, 1.001, 0.05)
vols, rts = [], []
for s in shares:
       w = pd.Series(0.0, index=rets.columns)
       w[comm] = (1 - s) / len(comm)
       w[tech] = s / len(tech)
       vols.append(float(np.sqrt(w @ cov @ w)))
       rts.append(float(w @ mu))

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(shares * 100, vols, color="tab:red", marker="o", label="Risk (volatility)")
ax1.set_xlabel("Share of portfolio in tech stocks (%)")
ax1.set_ylabel("Annualized volatility", color="tab:red")
ax2 = ax1.twinx()
ax2.plot(shares * 100, rts, color="tab:green", marker="s", label="Return")
ax2.set_ylabel("Annualized return", color="tab:green")
i = int(np.argmin(vols))
ax1.axvline(shares[i] * 100, linestyle="--", color="gray")
ax1.set_title(f"Adding tech to a commodity portfolio (lowest risk at {shares[i]*100:.0f}% tech)")
ax1.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("mix_chart.png", dpi=150)
plt.show()