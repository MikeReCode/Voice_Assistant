import requests
import os
import dotenv

locations = {"brasov": {"lat": 45.664873, "lon": 25.562897},
             "bucuresti": {"lat": 44.4323, "lon": 26.1063},
             "ucea": {"lat": 45.7864, "lon": 24.6708},
             }


def weather(city):
    dotenv.load_dotenv()
    key = os.getenv("APY_KEY")
    city = locations[city]

    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&units=metric&appid={key}")

    print(r.json()["main"]["temp"], "°C")


if __name__ == '__main__':
    weather("ucea")
