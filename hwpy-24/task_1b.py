"""
Получение всех цен с динамического сайта маркетплейса с использованием Selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_all_prices(url):
    """
    Получает все цены с указанного динамического сайта маркетплейса.

    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)
        time.sleep(5)
        
        price_elements = driver.find_elements(By.CSS_SELECTOR, 'css_selector_price')
        prices = [element.text for element in price_elements]
        
    finally:
        driver.quit()
    
    return prices

if __name__ == "__main__":
    url = 'URL_динамического_сайта_маркетплейса'
    prices = get_all_prices(url)
    for price in prices:
        print(f"Цена: {price}")
