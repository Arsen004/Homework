"""
Получение погоды в Астане с использованием BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://example.com/weather/astana'

def get_weather_using_bs4(url):
    """
    Получает погоду в Астане с указанного URL, используя BeautifulSoup

    """
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_div = soup.find('div', class_='weather')
    weather_data = weather_div.text.strip() if weather_div else 'Информация о погоде не найдена'
    return weather_data

if __name__ == "__main__":
    weather = get_weather_using_bs4(URL)
    print(f"Погода в Астане: {weather}")
