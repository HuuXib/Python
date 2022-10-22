import time
import traceback

while True:
    name = input("Podaj swoje imie: ")
    if name != "":
        break
x = int(input("Podaj swój kod dostępu: "))

while x != 5432:
    print("Zły kod!")
    x = int(input("Podaj swój kod dostępu: "))


print ("Witamy w naszym banku", name)

srodki = 1000
print("Aktalne środki na koncie wynoszą:",srodki,"PLN")
z = int(input("Jaką kwotę chcesz wybrać?: "))

confirm = input("Czy na pewno chcesz wybrać podaną kwotę ze swojego konta bankowego TAK/NIE: ")
if confirm == "TAK":
    print("Pobieranie danych z serwera... ")
    time.sleep(4)

elif confirm == "NIE":
    print("Anulwoano wyciąg z konta")
    time.sleep(4)


print("----------------------------------------")
if z <= srodki:
    print("wybrano kwote o wartosci: ", z)
    print("Po wybraniu środków  na koncie zostało ",srodki - z,"PLN")
    print("Dziękujemy za korzystanie z usług naszego banku")

else:
    print("Zbyt małe środki na koncie. Aktualnie posiadanie środki: ",srodki," PLN")



