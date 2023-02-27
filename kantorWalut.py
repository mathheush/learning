import json
import requests

print("Witaj w kantorze walut.\n")
def welcome():

    x = input("Wpisz \"1\", jeśli chcesz sprzedać PLN.\n"
              "Wpisz \"2\", jeśli chcesz kupić PLN.\n"
              "Wpisz \"3\", jeśli chcesz zobaczyć aktualny kurs najpopularniejszych walut.\n"
              "Wpisz \"q\", aby zakończyć.\n"
              "Co chcesz zrobić?: "
              )
    if x == "1":
        sell()

    elif x == "2":
        exchange1()

    elif x == "3":
        currency()

    elif x == "q":
        pass

    else: print("Nieznana operacja. Spróbuj ponownie: \n"), welcome()

def currency():
    currency_all = ("EUR", "CHF", "USD", "GBP")
    print("\nOto aktualne kursy wybranych walut względem PLN:")
    print("Waluta    Sprzedaż    Kupno")
    for currency_id in currency_all:
        curr = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{currency_id}/2023-02-24/?format=json')
        curr = curr.json()
        curr = curr['rates']
        curr = curr[0]
        bid = curr.get('bid')
        ask = curr.get('ask')
        bid = float(round(bid, 2))
        ask = float(round(ask, 2))
        bid = str(bid)
        ask = str(ask)
        print(currency_id,"     ", bid,"      ",  ask )
    print("")
    welcome()

def sell():
    global amount
    amount = input("Ile chcesz sprzedać PLN:")
    if amount == "q":
        welcome()
    else:
        try: int(amount)
        except: print("Podaj prawidłową ilość lub wpisz \"q\" aby wrócić."), sell()
        else: exchange()

def exchange1():
    global p
    global id
    p = input("Wybierz na jaką walutę posiadasz:\n"
              "1. dolar amerykański\n"
              "2. euro\n"
              "3. funt\n"
              "4. frank szwajcarski\n")
    if p == "1":
        id = ("USD")
        buy()
    elif p == "2":
        id = ("EUR")
        buy()
    elif p == "3":
        id = ("GBP")
        buy()
    elif p == "4":
        id = ("CHF")
        buy()
    elif p == "q":
        welcome()
    else:
        print("Podaj prawidłową wartość lub wpisz \"q\" aby wrócić."), exchange1()

def buy():
    global amount
    global bid
    amount = input(f"Ile chcesz sprzedać {id}:")
    curr = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{id}/2023-02-24/?format=json')
    curr = curr.json()
    curr = curr['rates']
    curr = curr[0]
    bid = curr.get('bid')
    bid = float(round(bid, 2))
    print("Aktualny kurs wynosi:")
    print(bid, "PLN", "za 1", id)
    amount = int(amount)
    money = amount * bid
    money = float(round(money, 2))
    print("Otrzymasz", money, "PLN", "za", amount, id)

def exchange():
    global p
    global id
    p = input("Wybierz na jaką walutę chcesz wymienić:\n"
             "1. dolar amerykański\n"
             "2. euro\n"
             "3. funt\n"
              "4. frank szwajcarski\n")

    if p == "1":
        id = ("USD")
        ask()
    elif p == "2":
        id = ("EUR")
        ask()
    elif p == "3":
        id = ("GBP")
        ask()
    elif p == "4":
        id = ("CHF")
        ask()
    elif p == "q":
        welcome()
    else: print("Podaj prawidłową wartość lub wpisz \"q\" aby wrócić."), exchange()


def ask():
    global ask
    global amount
    curr = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{id}/2023-02-24/?format=json')
    curr = curr.json()
    curr = curr['rates']
    curr = curr[0]
    ask = curr.get('ask')
    ask = float(round(ask, 2))
    print("Aktualny kurs wynosi:")
    print(ask, "PLN", "za 1", id)
    amount = int(amount)
    money = amount / ask
    money = float(round(money, 2))
    print("Otrzymasz", money, id, "za", amount, "PLN")

welcome()
