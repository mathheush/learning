import json
import requests
import datetime

print("Witaj w aplikacji, która pozwoli Ci sprawdzić pogodę.\n")

def main():
    x = input("Wpisz \"1\", jeśli chcesz sprawdzić pogodę w danym mieście.\n"
              "Wpisz \"2\", aby wyświetlić pogodę (aktualne miasto: xxx).\n"
              "Wpisz \"3\", żeby zobaczyć pogodę w losowym mieście.\n"
              "Wpisz \"q\", by zakończyć.\n"
              "Co chcesz zrobić?: "
              )
    if x == "1":
        type_city()

    elif x == "2":
        deafult_city()

    elif x == "3":
        random_city()

    elif x == "q":
        pass

    else:
        print("Nieznana operacja. Spróbuj ponownie: \n"), main()


def location():
    global latitude, longitude, named
    city = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={typed_city}&count=10&language=en&format=json')
    city = city.json()
    named = city['results'][0]['admin3']
    latitude = city['results'][0]['latitude']
    longitude = city['results'][0]['longitude']


def weather():
    weather = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=weathercode,temperature_2m_max,temperature_2m_min&current_weather=true&timezone=Europe%2FBerlin&forecast_days=1')
    weather = weather.json()
    weather = weather['hourly']['temperature_2m']
    highest = max(weather)
    lowest = min(weather)
    x = datetime.datetime.now()
    x = (x.strftime("%H"))
    x = int(x)
    now = weather[x]
    print(f"{named}, aktualna temperatura wynosi {now}°C \n"
          f"Najniższa dziś wyniesie {lowest}°C"
          f", a z kolei najwyższ to {highest}°C"

    )

def type_city():
    global typed_city
    typed_city = input("Wpisz miasto z którego chcesz sprawdzić pogodę:\n")
    location()
    weather()

main()


