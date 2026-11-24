import yfinance as yf

df = yf.download("TCS.NS", start="2023-01-01")
print(df.head())