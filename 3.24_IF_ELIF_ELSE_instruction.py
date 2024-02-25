print("Jestem pierwsza linia.")
print("Jestem druga linia")
glodny = True

if glodny:
    print("Musze cos zjesc! ")
    print("Otwieram lodówkę...")
else:
    print("Jestem najedzony") # pojawi sie tylko w przypadku niespelnienia IF

# wcięcia w pythonie wynoszą 4 spacje
dzien = input("Wprowadź dzień tygodnia: ")

if dzien == 'Poniedzialek':
    print("Jest poniedzialek")
elif dzien == "Wtorek":
    print("Jest wtorek")
elif dzien == "Środa":
    print("Jest środa")
elif dzien == "Czwartek":
    print("Jest czwartek")
elif dzien == "Piątek":
    print("Jest piątek")
elif dzien == "Sobota":
    print("Jest sobota")
elif dzien == "Niedziela":
    print("Jest niedziela")
else:
    print("Nie zdefiniowano takiego dnia")