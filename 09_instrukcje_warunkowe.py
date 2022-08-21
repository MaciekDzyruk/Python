
light = input("Jakie jest światło? (red, green, yellow) ")

if light == 'red':
    print("Czekaj!")
elif light == 'yellow':
    print("Przygotuj się")
elif light == 'green':
    print("Ruszaj!")
else:
    print("Nieprawidłowy wybór, dostępne opcje: red, green, yellow")

    print("Jedź") if light == 'green' else print("Czekaj!") #uproszona forma powyższego działania

    

