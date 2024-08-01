"""
Получение курса валют с динамического сайта с использованием Selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_exchange_rate(url):
    """
    Получает курс валют с указанного динамического сайта.

    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)
        time.sleep(5)
        
        exchange_rate_element = driver.find_element(By.CSS_SELECTOR, 'css_selector_exchange_rate')
        exchange_rate = exchange_rate_element.text
        
    finally:
        driver.quit()
    
    return exchange_rate

if __name__ == "__main__":
    url = 'URL_динамического_сайта_с_курсом_валют'
    exchange_rate = get_exchange_rate(url)
    print(f"Курс валют: {exchange_rate}")
