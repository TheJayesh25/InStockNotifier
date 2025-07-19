# InStockNotifer

# 🛒 Telegram Stock Alert Bot (Amul Example)

This project is a lightweight, customizable Python bot that monitors product availability on any website and sends instant alerts via Telegram as soon as an item is back in stock.

Originally built to track the high-demand **Amul High Protein Lassi**, this solution is designed to solve a broader, real-world problem: missing out on products that sell out quickly.

Whether you're trying to buy limited-release sneakers, graphics cards, concert tickets, or grocery items — this tool ensures you're notified **faster than email** or broken "Notify Me" systems.

---

## 📦 Features

- ✅ Checks stock status for multiple product URLs
- ✅ Sends instant Telegram notifications when stock returns
- ⏰ Notifies repeatedly every 5 minutes for 30 minutes (optional behavior)
- 🔁 Resets if product goes out of stock again
- 🔧 Easily customizable for other use cases

---

## 🔧 Use Cases

This script isn't limited to Amul or dairy products — it can be used for:

- 🔔 Notifying when concert tickets go live
- 💻 Tracking graphics card restocks
- 📱 Monitoring smartphones / electronics on launch day
- 🛍️ Keeping tabs on flash sales or limited editions
- 👟 Sneaker drops, books, cosmetics, more...

---

## 📁 Project Structure

```
├── main.py # Main script
├── requirements.txt # Dependencies (requests, beautifulsoup4)
└── README.md # This file
```


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/amul-stock-checker.git
cd amul-stock-checker
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add your Telegram Bot credentials
In main.py, replace:

```
TELEGRAM_BOT_TOKEN = "your_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
```

with your actual values.

🔐 Tip:
You can also store these as environment variables for better security:

```
import os

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
```

Then set them before running:

```
set TELEGRAM_BOT_TOKEN=123456:ABCdef...
set TELEGRAM_CHAT_ID=123456789
python main.py
```

### ✉️ Telegram Setup
1. Search @BotFather on Telegram
2. Create a new bot → get your bot token
3. Search @userinfobot → get your Telegram chat ID
4. Start a conversation with your bot to allow it to message you

### 🔄 How It Works
- The script scrapes the product page(s) every 60 seconds.
- If a product is in stock:
   Sends an immediate alert.
   Sends follow-up reminders every 5 minutes for 30 minutes.
- Once a product is out of stock, the notification cycle resets.

### 🌐 Example Products Used

```
PRODUCTS = {
    "Amul High Protein Lassi (Plain, Pack of 30)": "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30",
    "Amul High Protein Lassi (Rose, Pack of 30)": "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"
}
```

Replace these with any product pages you want to monitor.

### 🧠 Extend This Project
- Add email alerts or WhatsApp API
- Log restock timestamps to a file or database
- Deploy 24/7 using Fly.io, Railway, or your own server
- Use UptimeRobot + Replit for free persistent hosting

---

### 🧑‍💻 Author
Jayesh Suryawanshi
- 🧠 Python Developer | 💡 AI Tools Builder | 🌍 Data & Engineering Enthusiast
- 📫 [LinkedIn](https://www.linkedin.com/in/jayesh-suryawanshi-858bb21aa/)

### 📄 License
MIT License – credit appreciated.
