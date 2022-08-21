name = "maciek"

print(len(name)) # funkcja len zwraca ilość znaków w podanej zmiennej typu string. W tym wypadku name jest argumentem metody len

#Metody do funkcje, które są przypisane do danego obiektu

print(name.capitalize()) #metoda capitalize nie przyjmuje argumentów. Zamienia pierwszą literę z małej na dużą

print(name.upper()) #metoda upper zmienia wszystkie litery na duże

print(name[0]) #wyświetlamy pierwszą literę zmiennej name.Indeksujemy zawsze od 0 a nie od 1

print(name[0:2]) #wyświetlamy dwie litery, 2 po : oznacza że chcemy wyświetlić 2 litery z name

print(name[2:]) #wyświetlamy litery od indexu 2 do końca

print(name[-2:]) #dwie litery od końca

channel = "Jak nauczyć się programowania"

print(channel.split(" ")) #metoda split dzieli stringa na pojedyncze słowa, argumentem jest znak który wskazuje na rozdzilność słów w naszym wypadku jest to spacja

join_string = "_"
print(join_string.join(['Gdzie', 'dówch', 'się', 'kłóci', 'tam', 'trzeci', 'korzysta.']))

print(name.startswith("m")) #sprawdzenie czy string zaczyna się określoną literą

print(name.endswith("i")) #jak wyżej ale na czy kończy się określoną litera

print(name.rstrip("k")) #usunięcie z prawej strony litery k
print(name.lstrip("m")) #odwrotnie z lewej strony litery m

print(name.strip()) #usuwa nadmierne spacje z przodu i z tyłu słowa

first_name = "Maciek"
last_nam = "Dzyruk"

print(first_name + " " + last_nam)

join_string = " "
print(join_string.join([first_name, last_nam]))

james_bond = 7
print(str(james_bond).zfill(3)) #argument metody zfill mówi z ilu znaków ma się składać nowy ciąg więc dodaje nam zera z przodu


