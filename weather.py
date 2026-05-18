import requests
import sys

API_KEY = "b1b15e88fa797225412429c1c50c122a1"

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Ошибка: {data.get('message', 'неизвестная')}")
        sys.exit(1)

    return data

def show_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    print("================================")
    print(f"Погода в: {city}, {country}")
    print("================================")
    print(f"Описание:    {desc}")
    print(f"Температура: {temp}°C (ощущается как {feels}°C)")
    print(f"Влажность:   {humidity}%")
    print("================================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        city = input("Введите город: ")
    else:
        city = " ".join(sys.argv[1:])
    data = get_weather(city)
    show_weather(data)