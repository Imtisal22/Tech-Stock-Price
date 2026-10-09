# Tech Stocks vs. Commodities: Portfolio Analysis

An analysis of ten technology stocks and three commodities (coffee, cocoa, sugar). It compares their returns and risk and shows how adding tech to a commodity portfolio changes overall risk.

Scenario: A small investment firm that specializes in coffee, cocoa and sugar wants to expand into technology companies. The goal is to compare returns and volatility, then recommend how to add tech stocks to the portfolio so that risk is kept as low as possible.

# Key findings

Tech earned much more than commodities. From January 2015, six of the ten tech stocks returned more than 20% a year. Coffee, cocoa and sugar returned only 3% to 6% a year, with a similar level of risk.
Tech and commodities barely move together. Daily correlations between a commodity and a tech stock were between 0.01 and 0.09.
Risk is lowest at about 40% tech.Moving from 0% to 40% tech cut annual volatility from 22.3% to 18.0% and raised the annual return from 4.8% to 11.4%.
Recommendation: hold 30% to 50% in tech for the lowest risk, or 70% to 80% for higher return at about today's level of risk. Spread the tech share across several companies.

 # Question and Answer 
Highest closing price (tech) : META, about $721 
Largest percentage gain since: NVDA, about 47,000% 

# Assets analyzed

 Group  Tickers 
Tech stocks:  AAPL, AMZN, BABA, CRM, META, GOOG, INTC, MSFT, NVDA, TSLA 
Commodity futures: KC=F (coffee), CC=F (cocoa), SB=F (sugar) 

Data source: [Yahoo Finance](https://finance.yahoo.com), downloaded with the `yfinance` library from 2015-01-01 to the most recent day available.

## Project structure

 get_data.py          # Downloads price data for all 13 assets into data/
 analysis.py          # Loads data, computes returns, volatility, correlations
 plot_monthly.py      # Chart: month-end closing prices of the tech stocks
 risk_return.py       # Chart: risk vs. return for all 13 assets
 portfolio_mix.py     # Table: portfolio return and risk as tech share rises
 mix_chart.py         # Chart: risk and return against tech share
 data/                # One CSV per asset (created by get_data.py)
 monthly_closes.png
 risk_return.png
 mix_chart.png
 Tech_Stocks_Portfolio_Report.docx   # Full written report
 README.md


## Requirements

- Python 3.9 or newer (developed with Python 3.12)
- Packages: `yfinance`, `pandas`, `numpy`, `matplotlib`

## Setup

1. Clone the repository and open a terminal in its folder:

   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   

2. (Optional) Create and activate a virtual environment.

   Windows (PowerShell):

   
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   

   macOS / Linux:

   
   python3 -m venv .venv
   source .venv/bin/activate
   

3. Install the packages:

   
   python -m pip install yfinance pandas numpy matplotlib
   

## How to run

Run the scripts in this order from the project folder.

1. Download the data. This creates a `data/` folder with 13 CSV files.

   
   python get_data.py
   

2. Summary statistics and correlations. Prints the last close, percentage gain, annual return, annual volatility and return per risk for each asset, then the correlation matrix.

   
   python analysis.py
   

3. Charts and portfolio mix. Each script saves a PNG (or prints a table) in the project folder.


   python plot_monthly.py
   python risk_return.py
   python portfolio_mix.py
   python mix_chart.py
   

## Method

1. Load daily closing prices for each asset.
2. Compute daily log returns. Annual return is the average daily return times 252. Annual volatility is the standard deviation of daily returns times the square root of 252.
3. Compute return per risk (annual return divided by annual volatility) to compare assets fairly.
4. Compute pairwise correlations of daily returns.
5. Build portfolios that start with equal parts coffee, cocoa and sugar, then move money into tech in 10% steps, with the tech share split equally among the ten stocks. Measure return and volatility for each mix, using only days on which all 13 assets traded.

## Results

![Month-end closing prices of the ten tech stocks](monthly_closes.png)

![Risk vs. return](risk_return.png)

![Risk and return as the tech share rises](mix_chart.png)

## Limitations

 Past performance does not predict future returns. Tech returned unusually well after 2015, partly because of a few winners such as NVDA and TSLA.
 Each group is split with equal weights. An optimized mix might do better but would depend more on past quirks.
 Commodity prices are futures prices. Contract changeovers can cause price jumps and may overstate volatility slightly.
 Volatility treats upward and downward moves alike. Costs, taxes and currency effects are not included.
 Correlations can rise sharply in a market crisis.

## Notes

`analysis.py` reads every CSV in `data/` and uses the file name as the ticker. Keep unrelated CSV files out of that folder.
If `get_data.py` is rate limited, wait a few minutes and rerun it, or update the library with `python -m pip install -U yfinance`.
  Facebook now trades as META, so the file is named `META.csv`.

## Report

The full report, written for a general audience, is in `Tech_Stocks_Portfolio_Report.docx`. It covers the motivation, steps, findings and conclusions.



