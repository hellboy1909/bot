from binance.client import Client
from config import binance_api_key, binance_api_secret

client = Client(binance_api_key, binance_api_secret)

def execute_trade(symbol, action):
    if action == "BUY":
        order = client.create_order(
            symbol=symbol,
            side='BUY',
            type='MARKET',
            quantity=0.001
        )
        return {"price": order['fills'][0]['price']}
    return {"price": None}