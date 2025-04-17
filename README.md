# 🪙 Gold Price Telegram Bot

A simple yet powerful Telegram bot that fetches the current gold price and sends it to your Telegram daily at **11:00 AM IST** using **GitHub Actions**.

---

## ✨ Features

- 📈 **Live Gold Price**: Automatically fetches the daily gold rate for 22kt.
- 🤖 **Telegram Bot Integration**: Sends updates directly to your Telegram.
- ⏰ **Scheduled Automation**: Runs daily at 11:00 AM IST via GitHub Actions.
- 🔐 **Secure Secrets**: Uses GitHub Secrets to store sensitive bot credentials.

---

## 🛠 Requirements

- Python 3.x
- Git
- Telegram Bot Token
- Telegram Chat ID

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aman-bits-pilani/gold-price-bot.git
cd gold-price-bot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create Your Telegram Bot

```bash
Search @BotFather in Telegram.
Send /newbot and follow the instructions.
Save the bot token provided.
```

### 4️⃣ Get Your Chat ID

-Send a message to your new bot.
-Open in browser:
```bash
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```
-Look for ```"chat":{"id":}``` in the JSON response.
