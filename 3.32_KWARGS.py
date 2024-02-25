def rzeczy(*args):
    print("=========================================")
    print("                  RZECZY                 ")
    print("=========================================")
    print("Wszystkie wpisane elementy to: ")
    for arg in args:
        print(arg)
    print(f'Pierwszy element to: {args[0]}')

# parametry nazwane kwargs oznaczają, że zawierają klucz i wartość do tego klucza
def dziennik(klasa,**kwargs):
    print("=========================================")
    print("                 DZIENNIK                ")
    print("=========================================")
    print(f'Klasa : {klasa}')
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get('Kowalski'))



rzeczy('lampa','koc','łóżko','telefon')
dziennik('3c',Kowalski = 1, Nowak = 2, Wisniewski = 3)