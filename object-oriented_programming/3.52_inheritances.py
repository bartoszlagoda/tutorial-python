class Osoba:

    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return f"Nazywam sie {self.imie} {self.nazwisko}"

class Student (Osoba): # klasa Student dziedziczy po klasie Osoba

    def __init__(self,imie,nazwisko,nr_indeksu):
        Osoba.__init__(self,imie,nazwisko)
        self.nr_indeksu = nr_indeksu

    def podaj_numer_indeksu(self):
        return self.nr_indeksu

    # 3.53 nadpisywanie metod klasy nadrzędnej w klasie podrzędnej
    def przedstaw_sie(self):
        return f"Jestem studentem i mam na imie {self.imie}"


osoba = Osoba("Tomasz","Kot")
student = Student("Eugeniusz","Bodo",123456)
print(osoba.przedstaw_sie()) # wywołanie metody z klasy nadrzędnej dla klasy podrzędnej
print(student.przedstaw_sie())
print(student.podaj_numer_indeksu())