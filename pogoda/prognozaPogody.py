import requests
import datetime
import random


print("Witaj w aplikacji, która pozwoli Ci sprawdzić pogodę.\n")

def main():
    with open("yourcity.txt") as f:
        yours_city = f.readlines()
    x = input("Wpisz \"1\", jeśli chcesz sprawdzić pogodę w danym mieście.\n"
              f"Wpisz \"2\", aby wyświetlić pogodę (aktualne miasto: {yours_city[0]})\n"
              "Wpisz \"3\", żeby zobaczyć pogodę w losowym mieście.\n"
              "Wpisz \"4\", by zmienić ustawione miasto.\n"
              "Wpisz \"q\", by zakończyć.\n"
              "Co chcesz zrobić?: "
              )
    if x == "1":
        type_city()
        main()

    elif x == "2":
        deafult_city()
        main()

    elif x == "3":
        random_city()
        main()

    elif x == "4":
        set_city()
        main()

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
    print(f"\n\n{named}, aktualna temperatura wynosi {now}°C \n"
          f"Najniższa dziś wyniesie {lowest}°C"
          f", a z kolei najwyższa to {highest}°C \n\n"

    )

def type_city():
    global typed_city
    typed_city = input("Wpisz miasto z którego chcesz sprawdzić pogodę:\n")
    location()
    weather()

def deafult_city():
    with open("yourcity.txt") as f:
        yours_city = f.readlines()
    global typed_city
    typed_city = yours_city[0]
    location()
    weather()

def set_city():
    change_city = input("Wpisz swoje miasto: ")
    save_city = open("yourcity.txt", "w")
    save_city.write(change_city)
    save_city.close
    print("\nTwoje miasto zostało zapisane!\n")

def random_city():
    global typed_city
    typed_city = ["Lódź", "Gdańsk", "Wrocław", "Częstochowa", "Zielona Góra", "Kraków", "Zakopane", "Berlin"]
    x = random.randint(-1, 7)
    typed_city = typed_city[x]
    location()
    weather()


main()
