# Słownik posiada klucz i wartość
dziennik = {1:"Kowalski",
            2:"Nowak",
            3:"Lewandowski"}

print(dziennik.get(1)) # wartość pod kluczem 1
print(dziennik[1]) # drugi sposób na uzyskanie wartości z klucza o numerze 1
dziennik[4] = "Mucha" # przypisanie nowej wartości pod nowym kluczem 4

for key in dziennik.keys(): # iterowanie po kluczach
    print(key)

for value in dziennik.values(): # iterowanie po wartościach
    print(value)

del dziennik[1] # usunięcie klucza 1 i jego wartości

for value in dziennik.values():
    print(value)

dziennik[2] = "Nowy uczen"
print("Nowy uczen to: " + dziennik[2])

# Klucze muszą mieć unikalne wartości

