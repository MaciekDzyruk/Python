# names_list = [] - tak wygląda pusta lista
#w ramach jednej listy grupujemy obiekty tego samego typu

names_list = []
names_list.append("Adam") #metoda append pozwala dodawać element do listy
names_list.append("Kamil")
names_list.append("Maciek")
names_list.append("Kamil")
names_list.append("Adam")
#names_list.sort()
print()
print("Policzmy ile razy imie Adam wysępuje w liście")
print(names_list.count("Adam"))

print("Lista imion: ")
print(names_list)
print()

print(len(names_list)) #długość listy imion

print("Lista cała")
print(names_list)
names_list.remove("Kamil")
print("Lista po zastosowaniu metody remove, która usunie pierwsze wystąpienie imienia Kamil w liście")
print(names_list)

car_brands = ["Opel", "Audi", "Ford", "Skoda"] #można też od razu dodać listę z wieloma elementami
car_brands.sort() # sortowanie powyższej listy
# car_brands.sort(reverse=True) sortowanie odwrotne
print("Marki aut: ")
print(car_brands)
print()

print("Tak działa pętla")
for brand in car_brands: #brand to zmienna do której zostaną przypisane poszczególne elementy listy
    print(brand)

print()
print("Tak działa odwrócenie listy")
car_brands.reverse() #odwrócenie listy
print(car_brands)


print("Tak działa wyświetlenie wybranego elementu listy")
print(car_brands[0]) # odwołanie się do  pierwszego elementu listy. Takie odwłoanie nie zmienia struktury listy
print("lista po usunięciu elementu z indexem 0")
#print(car_brands.pop(0))
#print(car_brands)

#car_brands.clear() #usuwa wszystkie elementy z listy
#print(car_brands)

car_brands2 = ["Volvo", "Fiat", "Jaguar"]

all_cars = car_brands + car_brands2
print(all_cars)





