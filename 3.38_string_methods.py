imie = 'Bartek'
nazwisko = "Kowalski 'Nowak '"
adres = '''Kwiatowa 28c/1
            Warszawa 00-001'''


print(nazwisko)
print('Czytam ksiazke "Władca Pierścieni"')
print('\\Czytam \t ksiazke \n  \"Władca Pierścieni\"')

print("małe litery na wielkie".upper())
print("DUZE LITERY NA MAŁE".lower())
print(imie.islower()) # sprawdza przez boolean czy litery są małe
print(nazwisko.isupper()) # sprawdza przez boolean czy litery są duże

for char in 'Bartek':
    print(char)

print(imie[0]) # B
print(imie[0:4]) # [0:4) pod koniec zakres otwarty
print(imie.index("a")) # na jakim indeksie jest a
print("Ala" in "Ala ma kota") # czy 'Ala' znajduje się w 'Ala ma kota'
print("Kasia" not in "Ala ma kota") # czy 'Kasia' nie znajduje się w 'Ala ma kota'
print(" ".join(["Ala","ma","kota"])) # połącz słowa z tablicy dzieląc je spacją
print("Ala ma kota i psa".split(" ")) # wrzuć słowa do tablicy poprzedzone spacją
print(imie.startswith("Ba")) # czy imie zaczyna sie od podanego ciagu znakow
print(imie.endswith("tek")) # czy imie konczy sie podanych ciagiem znakow
