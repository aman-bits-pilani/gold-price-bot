import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_to_telegram(price: str):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram credentials missing")
        return

    Bot(token=TELEGRAM_TOKEN).send_message(
        chat_id=CHAT_ID,
        text=f"💰 Malabar 22K Gold Price: {price}"
    )

def get_gold_price():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=opts)
    wait = WebDriverWait(driver, 30)

    try:
        driver.get("https://www.malabargoldanddiamonds.com/in/pan-india/en/live-gold-rate.html")

        print("Page loaded...")
        time.sleep(3)

        price_element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'22') and contains(text(),'K')]/following::*[contains(text(),'₹') or contains(text(),'INR')]")
            )
        )

        price = price_element.text.strip()

        print(f"Gold Price: {price}")
        send_to_telegram(price)

    except Exception as e:
        print(f"Error: {e}")

        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        print("Saved debug.html")

    finally:
        driver.quit()


if __name__ == "__main__":
    get_gold_price()
