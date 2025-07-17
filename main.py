import requests
from bs4 import BeautifulSoup
import time
import os

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

PRODUCTS = {
    "Plain Lassi": "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30",
    "Rose Lassi": "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"
}

HEADERS = {"User-Agent": "Mozilla/5.0"}

# === Stock Check Function ===
def is_in_stock(url):
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        button = soup.find("button", class_="btn btn-primary btn-block")
        return button and "Add to Cart" in button.text
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False


# === Telegram Alert Function ===
def send_telegram_alert(product_name, url):
    message = f"🛒 *{product_name}* is *BACK IN STOCK*!\n[Click here to buy]({url})"
    api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(api_url, data=data)

    # DEBUG: Print response
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        print(f"✅ Telegram alert sent for {product_name}")
    else:
        print("❌ Failed to send alert")


# === Main Loop ===
print("🔁 Starting stock monitor...")
from datetime import datetime, timedelta

notified_products = {}

# Constants
FOLLOW_UP_INTERVAL = 300  # 5 minutes in seconds
MAX_DURATION = 1800       # 30 minutes in seconds

while True:

    for name, url in PRODUCTS.items():

        if check_stock(url):

            if name not in notified_products:
                send_telegram_alert(name, url)
                notified_products.add(name)

        else:
            if name in notified_products:
                notified_products.remove(name)

    time.sleep(60)