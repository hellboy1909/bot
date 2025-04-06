import sqlite3
from datetime import datetime

conn = sqlite3.connect("trades.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    action TEXT,
    price REAL,
    timestamp TEXT
)
""")
conn.commit()

def save_trade(symbol, action, price):
    cursor.execute("INSERT INTO trades (symbol, action, price, timestamp) VALUES (?, ?, ?, ?)",
                   (symbol, action, price, datetime.now().isoformat()))
    conn.commit()