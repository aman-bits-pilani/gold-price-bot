import os
import time
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
    """Send today’s price to the configured Telegram chat."""
    Bot(token=TELEGRAM_TOKEN).send_message(
        chat_id=CHAT_ID,
        text=f"Today's Malabar 22K Gold Price: {price}",
    )

def get_gold_price() -> None:
    """Scrape Malabar’s site and push the price to Telegram."""
    options = Options()
    options.add_argument("--headless=new")          # Chrome >= 109
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    try:
        driver.get("https://www.malabargoldanddiamonds.com/goldprice")

        # Wait until the price element is present — safer than time.sleep
        price_span = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//span[contains(@class,'22kt-price')])[1]",
                )
            )
        )
        price = price_span.text.strip()

        if not price:
            raise ValueError("Price element found but text is empty")

        print(f"Gold Price: {price}")
        send_to_telegram(price)

    except Exception as exc:
        print(f"Error occurred: {exc}")

    finally:
        driver.quit()

if __name__ == "__main__":
    get_gold_price()
