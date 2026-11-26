# Indian Stock Analysis Dashboard

An interactive dashboard to analyze and compare Indian stocks (NSE)
using Python, Streamlit and Plotly.

## Features
- Price chart with 50-day and 200-day moving averages
- Key metrics: latest close and annualized volatility
- Multi-stock comparison with normalized prices
- Summary table of total return and volatility

## Tech Stack
Python, pandas, yfinance, Plotly, Streamlit

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Key Insights

- **Uptrend (2023 to mid-2024):** TCS rose from around ₹2,900 in Jan 2023 to nearly ₹4,200 by mid-2024. Throughout this period the 50-day moving average (MA50) stayed mostly above the 200-day moving average (MA200), a sign of a strong uptrend.
- **Peak and reversal (late 2024 to early 2025):** The price peaked near ₹4,200. After Jan 2025, MA50 fell below MA200 (a "death cross"), and a prolonged decline followed.
- **Downtrend (2025 to 2026):** The price fell to roughly ₹2,000, about 50% below its peak. For most of this time it traded below MA200, indicating weak momentum.
- **Recent recovery:** Since mid-2026 the price has been recovering and is moving back toward MA50 and MA200. If it holds above both averages, it could signal a trend reversal.
- **Lagging indicator:** Moving average crossovers (golden/death cross) signal *after* the price has already moved, so they are not reliable on their own for trading decisions. They work better when combined with indicators like volume and RSI.
- **Limitation:** This analysis is based only on historical data and is not investment advice.

## Screenshots
![Price Chart](screenshots/price_chart.png)
![Comparison](screenshots/comparison.png)

## Future Improvements
- Add RSI and Bollinger Bands
- Add more stocks and a search box
- Add a simple backtesting module