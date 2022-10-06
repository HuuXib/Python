import random

y = int(input("Podaj Liczbe od 1 do 100: "))
x = random.randrange(1, 100)

# if y > x:
#     print("Dana liczba jest mniejsza")
# elif y < x:
#     print("Dana liczba jest większa")
while x != y:
    if y > x:
        print("Dana liczba jest mniejsza")
    elif y < x:
        print("Dana liczba jest większa")

    y = int(input("Podaj Liczbe od 1 do 100: "))


else:
    print("Brawo! Udało ci się odgadnąć liczbę która wynosiła: ", x)




