import asyncio
import os
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from telegram import Bot

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

async def send_to_telegram(price):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=f"Today's Malabar 22K Gold Price: {price}")

def get_gold_price():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://www.malabargoldanddiamonds.com/goldprice")
        time.sleep(5)  # Wait for the page to load

        # Locate the element that contains the gold price
        price_element = driver.find_element(By.XPATH, "(//li/span[@class='price 22kt-price'])")  # XPath to the price
        price = price_element.text.strip()
        print(f"Gold Price: {price}")
        asyncio.run(send_to_telegram(price))  # Send the price to Telegram
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_gold_price()
