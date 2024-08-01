"""
Получение погоды в Астане с использованием string.split()
"""

import requests

URL = 'https://example.com/weather/astana'

def get_weather_using_split(url):
    """
    Получает погоду в Астане с указанного URL, используя string.split()

    """
    response = requests.get(url)
    response.raise_for_status()
    
    content = response.text
    parts = content.split('<div class="weather">')
    weather_data = parts[1].split('</div>')[0]
    return weather_data

if __name__ == "__main__":
    weather = get_weather_using_split(URL)
    print(f"Погода в Астане: {weather}")
