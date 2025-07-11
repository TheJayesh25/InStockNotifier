import requests
from bs4 import BeautifulSoup
import time

URL = "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def check_stock():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    button = soup.find("button", class_="btn btn-primary btn-block")

    if button:
        text = button.text.strip()
        if "Add to Cart" in text:
            print("Product is in stock")
        else:
            print("Out of stock")
    else:
        print("Could not find stock button")

while True:
    check_stock()
    print("Waiting before next check...")
    time.sleep(60)