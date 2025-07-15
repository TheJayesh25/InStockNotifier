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

def check_stock(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    button = soup.find("button", class_="btn btn-primary btn-block")

    if button and "Add to Cart" in button.text:
        return True
    return False


def send_telegram_alert(product, url):
    message = f"{product} is back in stock!\n{url}"

    api = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    requests.post(api, data=data)


notified_products = set()

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