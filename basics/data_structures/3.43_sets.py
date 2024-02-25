pierwszy_zbior = {"Warszawa","Katowice","Krakow","Lodz"}
drugi_zbior = {"Warszawa"}

pierwszy_zbior.add("Kielce") # dodanie elementu do pierwszego zbioru
print(pierwszy_zbior)

pierwszy_zbior.add("Lodz") # dodanie istniejacego juz elementu w zbiorze
print(pierwszy_zbior)

print(f"Pierwszy zbiór: {pierwszy_zbior}")
print(f"Drugi zbiór: {drugi_zbior}")

# Zbiory przechowują tylko elementy unikalne
# Zbiory nie mają indeksowania

# różnica zbiorów
print(f"Roznica zbiorow : {pierwszy_zbior - drugi_zbior}")
# suma zbiorów
print(f"Suma zbiorow : {pierwszy_zbior | drugi_zbior}")
# część wspólna dwóch zbiorów
print(f"Częśś wspólna zbiorów: {pierwszy_zbior & drugi_zbior}")
# różnica symetryczna
print(f"Różnica symetryczna zbiorów: {pierwszy_zbior ^ drugi_zbior}")