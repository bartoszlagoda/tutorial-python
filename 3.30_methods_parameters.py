# utworzenie metody
def pogoda():
    print("=====================")
    print("Informacje o pogodzie")
    print("=====================")
    print('Jest słonecznie')
    print('Temperatura wynosi 20 stopni')
    print('Nie pada deszcz')

def przedstawSie(imie, wiek):
    print("-------------------")
    print("Komunikat powitalny")
    print("-------------------")
    print(f'Cześć! Mam na imię {imie}')
    print(f'Mam {wiek} lat')

przedstawSie(input("Wprowadź swoje imię: "), input("Wprowadź swój wiek: "))
pogoda()  # wywołanie metody
