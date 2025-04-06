from telethon.sync import TelegramClient, events
from config import api_id, api_hash, bot_owner_id
from analysis.indicators import analyze_market
#from binance.binance_api import execute_trade
from binance.binance_api import execute_trade
from database.db import save_trade
import asyncio

client = TelegramClient('crypto_bot', api_id, api_hash)

@client.on(events.NewMessage(from_users=bot_owner_id, pattern='/analyze'))
async def handler(event):
    analysis = analyze_market()
    message = f"سیگنال تحلیل:\n{analysis['summary']}\n\nخرید؟ (بله/خیر)"
    await event.respond(message)

    response = await client.wait_for(events.NewMessage(from_users=bot_owner_id))
    if response.text.strip() == 'بله':
        trade_result = execute_trade(analysis['symbol'], analysis['action'])
        save_trade(analysis['symbol'], analysis['action'], trade_result['price'])
        await event.respond(f"خرید انجام شد: {trade_result}")
    else:
        await event.respond("خرید لغو شد.")

client.start()
client.run_until_disconnected()