print("===============================")
print("       DODAWANIE LICZB         ")
print("===============================")
while True:
    try:
        pierwsza_liczba = int(input("Podaj pierwszą liczbę: "))
        druga_liczba = int(input("Podaj drugą liczbę: "))
        print(f"Wynikiem dodawania {pierwsza_liczba} i {druga_liczba} jest {pierwsza_liczba + druga_liczba}")
        break
    except ValueError:
        print("Podałeś błędną wartość.")
        print("Spróbuj ponownie.")
        continue

