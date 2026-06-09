import requests
from datetime import datetime

API_KEY = "24fee085ef095aec11db5181294a8897"


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    return data


def display_weather(data):

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n========== WEATHER REPORT ==========")
    print("Date & Time :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("City        :", city_name)
    print("Temperature :", temperature, "°C")
    print("Humidity    :", humidity, "%")
    print("Weather     :", weather)
    print("Wind Speed  :", wind_speed, "m/s")
    print("====================================")


def save_report(data):

    with open("weather_reports.txt", "a") as file:

        file.write(
            f"""
Date: {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}
City: {data["name"]}
Temperature: {data["main"]["temp"]} C
Humidity: {data["main"]["humidity"]}%
Weather: {data["weather"][0]["description"]}
Wind Speed: {data["wind"]["speed"]} m/s
----------------------------------------
"""
        )


while True:

    city = input("\nEnter City Name : ")

    try:

        data = get_weather(city)

        if data["cod"] == 200:

            display_weather(data)

            save_report(data)

            print("\nReport Saved Successfully!")

        else:
            print("City not found!")

    except Exception as e:

        print("Error:", e)
    choice = input("\nDo you want to search another city? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank You!")
        break