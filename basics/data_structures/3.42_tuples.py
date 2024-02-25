jezyki_programowania=("js","php","java")

zmienna_1 = "js" # string
zmienna_2 = "js", # krotka
zmienna_3 = "js","php",1,2,3,True # krotka może mieć różne typy danych

print(f"Zmienna 1 jest typu: {type(zmienna_1)}")
print(f"Zmienna 2 jest typu: {type(zmienna_2)}")

print(f"Krotka o indeksie 0: {jezyki_programowania[0]}")
print(f"Krotka o indeksie -1: {jezyki_programowania[-1]}")
print(f"Krotki o indeksach [0,1): {jezyki_programowania[0:1]}")

# krotek nie da się nadpisywać
print(f"Typ danych zmiennej 'jezyki programowania' to : {type(jezyki_programowania)}")
