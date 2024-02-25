# definiowanie listy
imiona = ["Bartek", "Tomek", "Andrzej", 1, 2, 3, 4, 5] # nie ma ograniczenia co do typu danych
print(imiona[0]) # Bartek
print(imiona[6]) # 4
print(imiona[-1]) # 5 -> czyli 1 element od końca
print(imiona[0:4]) # Bartek, Tomek, Andrzej, 1
print(imiona.index("Bartek")) # 0

# dodawanie elementu do listy w konkretnym miejscu
imiona.insert(0, "Grzegorz") # indeks i parametr pod indeks
# Grzegorz nie nadpisze Bartka, tylko przesunie wszystko dalej

# dodawanie elementu do listy na ostatnie miejsce
imiona.append("Wojtek")
print(imiona)
print(len(imiona)) # długość listy

imiona.remove("Bartek") # usunięcie konkretnego elementu po jego wartości
del imiona[0] # usunięcie konkretnego elementu po jego indeksie

pierwsza_lista = ["lampa","koc","krzesło"]
print(pierwsza_lista * 3) # trzykrotnie pierwsza_lista

druga_lista = ["auto","młotek",1,2,3,4]
print(pierwsza_lista + druga_lista)

