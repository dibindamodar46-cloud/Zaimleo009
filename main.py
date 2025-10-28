import requests
import time
import datetime
from telegram import Bot

# Machan ScalpX System - Zaimleo009 Edition
BOT_TOKEN = "8479683444:AAGg22ODrfa4olHiELpF9qETWAvoSyp8ZjM"
CHAT_ID = "940758967"
bot = Bot(token=BOT_TOKEN)

def get_nifty_data():
    return {
        "price": 22230,
        "vwap": 22210,
        "oi_trend": "positive",
        "support": 22180,
        "resistance": 22280
    }

def check_signal(data):
    price = data["price"]
    vwap = data["vwap"]
    if price > vwap and data["oi_trend"] == "positive":
        return "CALL"
    elif price < vwap and data["oi_trend"] == "negative":
        return "PUT"
    else:
        return None

def send_alert(signal, data):
    msg = (
        f"⚡ *Zaimleo009 Alert*\n"
        f"Type: {signal}\n"
        f"NIFTY Price: {data['price']}\n"
        f"VWAP: {data['vwap']}\n"
        f"Support: {data['support']} | Resistance: {data['resistance']}\n"
        f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}"
    )
    bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")

while True:
    data = get_nifty_data()
    signal = check_signal(data)
    if signal:
        send_alert(signal, data)
    time.sleep(60)
