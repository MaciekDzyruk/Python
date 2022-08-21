print("Wszystkie podawane niżej liczby muszą być od siebie różne")
a = int(input("Wprowadź wartość dla a: "))
b = int(input("Wprowadź wartość dla b: "))
c = int(input("Wprowadź wartość dla c: "))

if a > b and a > c:
    print("a jest największe z wprowadzonych liczb")
elif b > a and b > c:
        print("b jest największe z wprowadzonych liczb")
elif c > a and c > b:
    print("c jest największe z wprowadzonych liczb")
else:
    print("Wprowadzaona nieprawidłową wartość")

