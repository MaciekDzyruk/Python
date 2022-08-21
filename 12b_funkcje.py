def display_sum(a, b): # ta funcja przyjmuje dwa argumenty a i b
    print(a+b) # i wyświetla na ekranie sumę tych dwóch argumentów ale niczego nam nie zwraca

display_sum(10, 20) # ta funkcja nic nie zwraca tylko przyjmuje argumenty

def calculate_sum(a, b): # ta funcja przyjmuje dwa argumenty a i b
    return a + b # zwraca sumę a + b

sum = calculate_sum(2, 3)
print(sum)

def print_message(): # ta funkcja niczego nie przyjmuje ani nie zwraca
    print("Text message")

print_message()