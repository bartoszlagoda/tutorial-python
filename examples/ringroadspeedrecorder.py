from datetime import datetime

# Główna funkcja, to w niej się wszystko dzieje
def main():
    try:
        while True:
            entry = input()
            table_input = entry.split()
            if test(table_input):
                print(f"{view_registration(table_input)} {or_a_ticket(table_input)} {average_speed(table_input):.2f}")
            else:
                print("BLAD")
    except EOFError: # przerwanie gdy koniec pliku lub zakończenie programu
        pass

# Funkcja wyświetlająca komunikaty
def test(table_input):
    return len(table_input) == 5 and car_registration(table_input) and car_or_truck(table_input) \
           and distance(table_input) and start(
        table_input) and stop(table_input)

# Funkcja testuje poprawność danych dla rejestracji
def car_registration(table_input):
    rej = table_input[0]
    if len(rej) != 6:
        return False
    elif rej[0:2].isalpha() != True: # czy same litery
        return False
    elif rej[0:2].isupper() != True: # czy duze znaki
        return False
    elif rej[2:6].isdigit() == True: #czy sama liczba
        return True
    else:
        return False

# Funkcja sprawdzająca poprawność danych dla typu pojazdu (S lub C)
def car_or_truck(table_input):
    cot = table_input[1]

    if len(cot) != 1:
        return False
    elif cot.isalpha() != True:
        return False
    elif cot.isupper() != True:
        return False
    elif cot not in ["S", "C"]:
        return False
    else:
        return True

# Funkcja sprawdzająca poprawność wprowadzonej przejechanej odległości
def distance(table_input):
    dist = table_input[2]

    if dist.isdigit() != True:
        return False
    else:
        return True

# Funkcja testująca czas początkowy
def start(table_input):
    z = table_input[3]

    if len(z) != 5:
        return False
    elif z[2] != ":":
        return False
    elif z[0:2].isdigit() == False:
        return False
    elif z[3:5].isdigit() == False:
        return False
    elif int(z[0:2]) >= 24:
        return False
    elif int(z[3:5]) >= 60:
        return False
    else:
        return True

# Funkcja testująca czas końcowy
def stop(table_input):
    r = table_input[4]
    if len(r) != 5:
        return False
    elif r[2] != ":":
        return False
    elif r[0:2].isdigit() == False:
        return False
    elif r[3:5].isdigit() == False:
        return False
    elif int(r[0:2]) >= 24:
        return False
    elif int(r[3:5]) >= 60:
        return False
    else:
        return True

# Funkcja obliczająca średnią prędkość
def average_speed(table_input):
    initial_speed = table_input[3]
    final_speed = table_input[4]

    # metry na kilometry
    ile_km = int(table_input[2]) / 1000

    # zmiana typu string na datatime
    start_hour = datetime.strptime(initial_speed, "%H:%M")
    end_hour = datetime.strptime(final_speed, "%H:%M")

    # obliczenie różnicy w czasach końcowym i początkowym
    travel_time = (end_hour - start_hour).seconds # różnica w sekundach
    travel_time_m = travel_time/3600 # różnica w godzinach
    hmk = ile_km / travel_time_m
    return hmk

# rejestracja samochodowa do wyświetlenia
def view_registration(table_input):
    i = table_input[0]
    return i

# sprawdza koniecznosc wystawienia mandatu
def or_a_ticket(table_input):

    if table_input[1] == "S" and average_speed(table_input) > 120:
        return "M"
    elif table_input[1] == "C" and average_speed(table_input) > 80:
        return "M"
    else:
        return "."


if __name__ == '__main__':
    main()