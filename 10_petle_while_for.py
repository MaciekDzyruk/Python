#pętla while to pętla która wykonuje się dopóki nie zostanie spełniony określony warunek

number = 1
number2 = 1

#while number < 6:
    #print(number)
    #number += 1

for number2 in range(0, 20, 2):    #zakres z lewej domknięty a z prawej otwarty Range może przyjmować 3 argument tzw. krok czyli o ile jest skok
    if number2 == 4:
        #break z powyższym warunkiem zatrzyma się po 0,2
        continue #continue przerywa aktualne wywołanie pętli (nie przechodzi do printa) i przechodzi do kolejnego wywołania
    print(number2)