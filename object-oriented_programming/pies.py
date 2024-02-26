class Pies:
    gatunek = 'pies domowy'

    # konstruktor
    def __init__(self,rasa,imie,wiek): # pola te muszą być zadeklarowane w obiekcie klasy
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

# tworzenie obiektu klasy Pies
reksio = Pies('kundelek','Reksio',2)
print(reksio.wiek)
print(reksio.imie)
print(reksio.rasa)
print(reksio.gatunek)
print(Pies.gatunek) # poniewaz pole gatunek jest charakterystyczne dla calej klasy