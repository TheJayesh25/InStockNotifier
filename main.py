import requests
from bs4 import BeautifulSoup
import time

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


while True:
    for name, url in PRODUCTS.items():
        available = check_stock(url)

        if available:
            print(f"{name} is available")
        else:
            print(f"{name} is out of stock")

    print("Sleeping...")
    time.sleep(60)