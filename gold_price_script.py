import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_to_telegram(price: str) -> None:
    """Push today’s 22 K rate to Telegram."""
    Bot(token=TELEGRAM_TOKEN).send_message(
        chat_id=CHAT_ID,
        text=f"Today's Malabar 22K Gold Price: {price}"
    )

def get_gold_price() -> None:
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=opts)
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.malabargoldanddiamonds.com/in/pan-india/en/live-gold-rate.html")

        # Wait until 22K label is visible
        price_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'22k') or contains(text(),'22K')]/following::*[contains(text(),'INR')]")
            )
        )

        price = price_element.text.strip()

        print(f"Gold Price: {price}")
        send_to_telegram(price)

    except Exception as exc:
        print(f"Error occurred: {exc}")

    finally:
        driver.quit()

if __name__ == "__main__":
    get_gold_price()
