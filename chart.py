import yfinance as yf
import plotly.express as px

df = yf.download("TCS.NS", start="2023-01-01")

# MultiIndex columns ko simple bana do
df.columns = df.columns.get_level_values(0)


df["Return"] = df["Close"].pct_change()
df["MA50"] = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()


# Pehla chart
fig = px.line(df, x=df.index, y="Close", title="TCS Stock Price")
fig.show()

fig = px.line(df, x=df.index, y=["Close", "MA50", "MA200"],
              title="TCS Price with Moving Averages")

fig.update_layout(yaxis_title="Price (INR)", legend_title="Series")
fig.show()