name = input("Podaj swoje imie: ")
x = int(input("Podaj swój kod dostępu: "))

while x != 5432:
    print("Zły kod!")
    x = int(input("Podaj swój kod dostępu: "))


print ("Witamy w naszym banku", name)

srodki = 1000
print("Aktalne środki na koncie wynoszą:",srodki,"PLN")
z = int(input("Jaką kwotę chcesz wybrać?: "))

print("----------------------------------------")
if z <= srodki:
    print("wybrano kwote o wartosci: ", z)
    print("Po wybraniu środków  na koncie zostało ",srodki - z,"PLN")
    print("Dziękujemy za korzystanie z usług naszego banku")

else:
    print("Zbyt małe środki na koncie. Aktualnie posiadanie środki: ",srodki," PLN")
