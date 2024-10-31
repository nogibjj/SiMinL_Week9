from mylib.lib import load, summary, chart, candlestick
import yfinance as yf

natgas = yf.Ticker("NG=F")
df = natgas.history(interval="1d", start="2024-01-02")

if __name__ == "__main__":
    load(df)
    summary(df)
    chart(df)
    candlestick(df)
