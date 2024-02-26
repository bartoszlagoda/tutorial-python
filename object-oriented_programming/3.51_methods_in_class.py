class Pies:
    gatunek = 'pies domowy'

    # konstruktor
    def __init__(self,rasa,imie,wiek): # pola te muszą być zadeklarowane w obiekcie klasy
        print("====================")
        print("Wewnatrz metody init")
        print("====================")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self): # self - odwołanie się do konkretnych pól danego obiektu
        return "===========================\nPREZENTACJA UMIEJETNOSCI\n===========================\nHau Hau"

    def zaprezentuj_psa(self):
        print("====================")
        print(f"PIES {self.imie}")
        print("====================")
        print("Rasa to " + self.rasa)
        print("Imie to " + self.imie)
        print("Wiek psa to " + str(self.wiek))

# tworzenie obiektu klasy Pies
reksio = Pies('kundelek','Reksio',2)
print(reksio.wiek)
reksio.wiek = 3
print(reksio.wiek)
print(reksio.gatunek)
reksio.gatunek = "Ptak"
print(reksio.gatunek)
print(Pies.gatunek) # poniewaz pole gatunek jest charakterystyczne dla calej klasy
print(reksio.zaprezentuj_psa())
print(reksio.szczekaj())
