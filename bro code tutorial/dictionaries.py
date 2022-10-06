

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'Poland':'Warsaw','United Kingdom':'London'})
capitals.pop('China')
capitals.clear()

# print(capitals['Russia'])

# print(capitals.get('Germany'))
# wyswietla zawartosc danego słownika(klucza) ale bez błędu w przypadku wybrania paskudnego klucza

# print(capitals.keys())
# wyswietla klucze (nazwy) słowników

# print(capitals.values())
# wyswietla wartosci słownika

# print(capitals.items())
# wyswiatla nazwy słowników i ich zawartosc

for key,value in capitals.items():
    print(key, value)

# za pomocą fora wyswietla kolejno klucz i wartosc danego klucza