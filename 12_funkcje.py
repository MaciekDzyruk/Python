countries_information = {} #deklaracja słownika
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

#jako klucze słownika mamy nazwę kraju, jako wartości mamy krotki.

def show_country_info(country): #definicja funkcji, ta funkcja nic nie zwraca, przyjmuje "country" a następnie pobiera odpowiednią wartość a następnie wyświetla
    country_information = countries_information.get(country)
    print()
    print(country)
    print("----------")
    print("Stolica " + country_information[0])
    print("Liczba mieszkańców (mln): " + str(country_information[1]))

for country in countries_information.keys():
    print(country)

country = input("Informacje o jakim kraju chcesz wyświetlić? ")

show_country_info(country)


