def rzeczy(*args):
    print("Wszystkie wpisane elementy to: ")
    for arg in args:
        print(arg)
    print(f'Pierwszy element to: {args[0]}')


rzeczy('lampa','koc','łóżko','telefon')