import matplotlib.pyplot as plt
from analysis import load_prices, summarize

prices = load_prices("data")
s = summarize(prices)
commodities = ["CC", "KC", "SB"]

fig, ax = plt.subplots(figsize=(10, 7))
for name, row in s.iterrows():
       color = "tab:orange" if name in commodities else "tab:blue"
       ax.scatter(row["ann_volatility"], row["ann_return"], color=color, s=80)
       ax.annotate(name, (row["ann_volatility"], row["ann_return"]),
                   textcoords="offset points", xytext=(6, 6))

ax.scatter([], [], color="tab:blue", label="Tech stocks")
ax.scatter([], [], color="tab:orange", label="Commodities")
ax.set_xlabel("Annualized volatility (risk)")
ax.set_ylabel("Annualized return")
ax.set_title("Risk vs. return: tech stocks and commodities")
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig("risk_return.png", dpi=150)
plt.show()