name = 'Bartek' # zmienna globalna
surname = 'Nieznany'

def intrudouce_yourself():
    global surname # nadpisze zmienną globalną po wywołaniu tej metody
    surname = 'Kowalski' # zmienna lokalna
    print("Nazwisko przekazane lokalnie w metodzie: " + surname)
    print("Imie przekazane lokalnie w metodzie: " + name)


print("Imie przekazane globalnie: " + name)
print("Nazwisko przekazane globalnie: " + surname)
intrudouce_yourself()
print("Nazwisko przekazane globalnie po wywołaniu metody introduce_yourself() : " + surname)
