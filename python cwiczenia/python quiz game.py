print("Witam w moim quizie na temat Minecrafta")
answer = input('Chesz zagrac w quiz?(Tak/Nie): ')
wynik = 0
liczba_pytan = 3

if answer.lower()=='tak':
    answer=input('Pytanie nr1: Na początek jaka jest maksymalna liczba chunków możliwych do zrenderowania w opcjach gry (podaj sam numer): ')
    if answer.lower()=='128':
        wynik += 1
        print('Prawidłowa odpowiedź! Maksymalna liczba chunków możliwych do zrenderowania w opcjach gry wynosi 128 chunków ')
    else:
        print("zła odpowiedź")

    answer=input('Pytanie nr2: Jaki jest najnowszy biom dodany w wersji 1.19 do Minecrafta ? (chodzi o ten z wardenem): ')
    if answer.lower() =='deep dark':
        wynik += 1
        print("Zgadza sie najnowszy biom dodany w wersji 1.19 do Minecrafta to Deep Dark")
    else:
        print('Niestety ale twoja odpowiedź jest zła. Najnowszy biom dodany do Minecraft to Deep Dark')

    answer=input('Pytanie nr3: Wymień jeden spośród podanych elementów , które są niezbędne do zrobienia farmy Endermanów (trapdoor,endermit,soulsand,obsydian): ')
    if answer.lower() =='endermit':
        print("Zgadza się! Endermity są potrzebne aby Endermani mogli się na kimś ztriggerować oraz spadać z danej platformy: ")
        wynik += 1
    else:
        print("Żle! Prawidłowa odpowiedź to endermit")

else:
    print("Nastąpił błąd podczas próby dołączenia ")

print("----------------------------------------------------------")

print("Dziękujemy za zagranie w moją grę na temat minecrafta. Odpowiedziałeś na ",wynik,"pytań poprawnie")
odpowiedz = (wynik/liczba_pytan)
print("Błędy popełnione",odpowiedz)
print("To by było na tyle. Dzięki za gre!")


