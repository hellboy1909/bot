from pybit.unified_trading import HTTP
from config import bybit_api_key, bybit_api_secret

# اتصال به Bybit (حالت تست فعال یا واقعی)
session = HTTP(
    testnet=True,  # برای تست True، برای خرید واقعی False بذار
    api_key=bybit_api_key,
    api_secret=bybit_api_secret
)

def execute_trade(symbol, action):
    if action == "BUY":
        order = session.place_order(
            category="linear",
            symbol=symbol,
            side="Buy",
            order_type="Market",
            qty=0.001,
            time_in_force="GoodTillCancel"
        )
        return {"price": order.get("result", {}).get("order_price", "نامشخص")}
    return {"price": None}