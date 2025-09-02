import requests
import telebot
import time

# توکن رباتت
TOKEN = "8265595358:AAHrd4PwZ9yFGZZt4lkxco16wIY2E_sqv_0"
bot = telebot.TeleBot(TOKEN)

# آی‌دی کانال (باید ربات رو به عنوان ادمین کانال اضافه کنی)
CHANNEL_ID = "@GoldpriceChannel"  # اینو عوض کن به یوزرنیم کانالت

def get_gold_price():
    url = "https://api.metals.live/v1/spot"
    data = requests.get(url).json()
    # داده‌ها شامل طلا، نقره و ... هستن
    gold_price = data[0]['gold']
    return gold_price

# ارسال قیمت هر 1 دقیقه
while True:
    try:
        price = get_gold_price()
        bot.send_message(CHANNEL_ID, f"💰 قیمت لحظه‌ای اونس طلا: {price} دلار")
    except Exception as e:
        print("خطا:", e)
    time.sleep(60)
