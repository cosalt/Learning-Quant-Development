import yfinance as yf

# data frame for S&P 500 ETF
df = yf.download("SPY")
print(df.head())