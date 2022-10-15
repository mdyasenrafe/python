import requests
import json
import time

url = 'https://api.openweathermap.org/data/2.5/weather?q=chittagong&appid=55a46ecc32e557234eeaa584b270c635'


def weather_data():
    res = requests.get(url)
    content = res.content.decode('UTF-8')
    dict_conent = json.loads(content)
    return dict_conent


weather = weather_data()
print(weather)


while True:
    time.sleep(1800)
    weather = weather_data()
    print(weather)
