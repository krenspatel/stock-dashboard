import pandas as pd
import yfinance as yf
import plotly.express as px
import streamlit as st
import datetime

st.title("Indian Stock Analysis Dashboard")

stocks = {
    "TCS": "TCS.NS",
    "Reliance": "RELIANCE.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
}

name = st.selectbox("Stock choose karo", list(stocks.keys()))
start = st.date_input("Start date", value=datetime.date(2023, 1, 1))

@st.cache_data
def load_data(ticker, start):
    df = yf.download(ticker, start=start)
    df.columns = df.columns.get_level_values(0)
    df["Return"] = df["Close"].pct_change()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    return df



df = load_data(stocks[name], start)

fig = px.line(df, x=df.index, y=["Close", "MA50", "MA200"],
              title=f"{name} Price with Moving Averages")
fig.update_layout(yaxis_title="Price (INR)", legend_title="Series")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Latest Close", f"₹{df['Close'].iloc[-1]:.2f}")
col2.metric("Volatility (annual)", f"{df['Return'].std() * (252 ** 0.5):.2%}")

st.subheader("Stock Comparison")

selected = st.multiselect(
    "Compare karne ke liye stocks choose karo",
    list(stocks.keys()),
    default=["TCS", "Infosys"],
)

if len(selected) >= 2:
    prices = pd.DataFrame(
        {n: load_data(stocks[n], start)["Close"] for n in selected}
    ).dropna()

    # Sabko 100 se start karo
    normalized = prices / prices.iloc[0] * 100

    fig2 = px.line(normalized, title="Normalized Price (Start = 100)")
    fig2.update_layout(yaxis_title="Normalized Price", legend_title="Stock")
    st.plotly_chart(fig2, use_container_width=True)

    # Summary table
    summary = pd.DataFrame({
        "Total Return (%)": (prices.iloc[-1] / prices.iloc[0] - 1) * 100,
        "Annual Volatility (%)": prices.pct_change().std() * (252 ** 0.5) * 100,
    }).round(2)
    st.dataframe(summary)
else:
    st.info("Comparison ke liye kam se kam 2 stocks choose karo.")      