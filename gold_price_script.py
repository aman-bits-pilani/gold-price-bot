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
    """Open site, click Submit, scrape price, notify Telegram."""
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.malabargoldanddiamonds.com/goldprice")

        # 1️⃣  Wait for the Submit button, then click it
        submit_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit.gold-rate-btn"))
        )
        submit_btn.click()

        # 2️⃣  Wait until the 22 K price span contains non‑empty text
        price_span = wait.until(
            lambda d: (
                p := d.find_element(By.XPATH, "//span[@class='price 22kt-price']")
            ).text.strip() and p
        )
        price = price_span.text.strip()

        print(f"Gold Price: {price}")
        send_to_telegram(price)

    except Exception as exc:
        print(f"Error occurred: {exc}")

    finally:
        driver.quit()

if __name__ == "__main__":
    get_gold_price()
