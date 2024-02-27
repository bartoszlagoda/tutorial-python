def pogoda_krakow():
    return "Slonecznie"


def pogoda_szczecin():
    return "Pochmurno"


def pogoda_wroclaw():
    return "Upal"

if __name__ == '__main__': # specjalna zmienna name jest równa main tylko dla skryptów odpalanych bezpośrednio
    print(pogoda_krakow())
    print(pogoda_szczecin())
    print(pogoda_wroclaw())