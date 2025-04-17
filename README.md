# 🪙 Gold Price Telegram Bot

This repository contains a Telegram bot that fetches the current gold price and sends it to users via Telegram. The bot is powered by a Python script that scrapes the latest gold price from the **Malabar Gold and Diamonds website** and sends it to the specified Telegram chat.

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

- Send a message to your new bot.
- Open in browser:

```bash
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```
-Look for ```"chat":{"id":}``` in the JSON response.

---

## 🔐 Add GitHub Secrets

- Go to your repo → Settings → Secrets and Variables → Actions:
- Name | Value
- TELEGRAM_TOKEN | Your Telegram bot token
- CHAT_ID | Your chat ID from Telegram

---

## 🧪 Run Locally

```bash
python gold_price_script.py
```

- This will fetch the current gold price and send it to your Telegram chat.

---

## ⚙️ GitHub Actions Workflow

- The automation is defined in:
```bash
.github/workflows/gold_price.yaml
```
### Triggers:
- ⏰ **Scheduled:** Daily at 11:00 AM IST (30 5 * * * UTC)
- 🔘 **Manual:** via GitHub → Actions → Run workflow

---

## 📁 Project Structure

```bash
.
├── gold_price_script.py     # Main script
├── requirements.txt         # Python dependencies
└── .github/
    └── workflows/
        └── gold_price.yml   # GitHub Actions workflow
```
---
