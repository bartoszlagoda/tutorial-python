# Niedozwolone operacje:
#     print("1" + 1) -> zauważono tu różne typy danych

print("1" + str(1)) # konwersja na string
print(2 + int('2')) # konwersja na integer

print(2 + 2.4) # int z float nie będzie miał problemów
print(2 + float('2.4'))
# print(2 + int('2.4')) # taka konwersja się nie uda

# print('Moj tekst ' * 'Ala') # mnozenie stringów jest niedozwolone
print("Moj test " * int('5'))


