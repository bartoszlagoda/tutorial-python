def rzeczy(*args):
    print("Wszystkie wpisane elementy to: ")
    for arg in args:
        print(arg)
    print(f'Pierwszy element to: {args[0]}')

# parametry nazwane kwargs oznaczają, że zawierają klucz i wartość do tego klucza
def dziennik(klasa,**kwargs):
    print(f'Klasa : {klasa}')



rzeczy('lampa','koc','łóżko','telefon')