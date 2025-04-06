import requests
import pandas as pd
import ta

def analyze_market():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
    data = requests.get(url).json()
    prices = [p[1] for p in data["prices"]]
    df = pd.DataFrame(prices, columns=["close"])
    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    rsi = df["rsi"].iloc[-1]

    action = "BUY" if rsi < 30 else "SELL" if rsi > 70 else "HOLD"
    return {
        "symbol": "BTCUSDT",
        "rsi": round(rsi, 2),
        "action": action,
        "summary": f"RSI: {rsi:.2f}, پیشنهاد: {action}"
    }