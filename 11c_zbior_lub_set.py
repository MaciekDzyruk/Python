#set jest bardzo podobny do listy ale nie możemy mieć w nim danych zduplikowanych

names_set = {} #wydawać by się mogło, że to pusty set a w rzeczywistości jest to słownik
names_set = set() #Tak tworzymy pusty set
names_set = {"Maciek", "Adam", "Maciek"}

print(names_set)

car_brands = set()
car_brands.add("Audi")
car_brands.add("Opel")
car_brands.add("Ford")

print(car_brands)

car_brands.remove("Opel") #jeśli podany tu element jaki nie istnieje otrzymay error, że taki klczu nie istnieje
car_brands.discard("Ford") #jeśli podamy element jaki nie istnieje to nic się nie wydarzy

car_brands.add("Opel")
car_brands.add("Ford")

#print(names_set[0]) # takie wywołanie konkretnego rekordu z setu nie zadziała gdyż jest to zbiór nieuporządkowany
for car in car_brands:
    print(car)

    #dodając elementy do setu nie możemy być pewni w jakiej kolejności zostaną one zwrócone
    #elementy dodane do setu muszą być niemutowalne


#names_list = []
#names_tuple = ()
#names_set.add(names_list) pojawi się błąd
#names_set.add(names_tuple) krotka doda się do setu
#print(name_set) to wyświetli się set z dodaną do środka krotką

#Trzy podstawowe cechy setu:
# brak zduplikowanych wartości
# elementy setu muszą być niemutowalne
# elementy setu nie są uporządkowane

print(car_brands)

car_brands2 = {"Mazda", "Honada", "Nissan"}
print(car_brands2)

car_brands_total = car_brands.union(car_brands2) #union pozwala nam połączyć ze sobą dwa sety
print(car_brands_total)

#car_brands.update(car_brands2) #jeśli nie chcemy dodawać do siebie dwóch setów w nowej zmiennej możemy metodą update zaaktualizować jeden set o drugi

# print(car_brands)

cars = car_brands.difference(car_brands2)
print(cars)

#car_brands.intersection - szuka części wspólnych obu setów
# element jakie nie występują w jednym i w drugim zbiorze funkcja .symetric_difference

#car_brands.clear() usuwa wszystko z set

list_one = ["1", "2", "3"]
set_one = {"3", "4", "5"}

list_one.extend(set_one) #rozszerzenie listy o zawartość setu

print(list_one)











