import matplotlib.pyplot as plt
from analysis import load_prices

tech = ["AAPL","AMZN","BABA","CRM","META","GOOG","INTC","MSFT","NVDA","TSLA"]
prices = load_prices("data")
monthly = prices[tech].resample("ME").last()

monthly.plot(figsize=(12, 6), logy=True)
plt.title("Month-end closing price of 10 tech stocks (log scale)")
plt.ylabel("Close price (USD)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_closes.png", dpi=150)
plt.show()