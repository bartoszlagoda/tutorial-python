# Tryby:
# w - write
# a - append (dodajemy kiedy chcemy dopisywać wiadomości, a nie je nadpisywać)

def overwrite_file(path,message):
    file = open(f"../../resources/{path}", "a")
    file.write(
        "\n" + message)  # metoda zapisu do pliku ze zmiennej file
    # każda zmiana tekstu nadpisze poprzedni tekst
    file.close()

def add_to_file(path,message):
    file = open(f"../../resources/{path}", "w")
    file.write(message)  # metoda zapisu do pliku ze zmiennej file
    # każda zmiana tekstu nadpisze poprzedni tekst
    file.close()


add_to_file("3.48_create_new_message2.txt","Zapis z metody do calkiem nowego pliku.")
overwrite_file("3.48_create_new_message.txt","Dodawanie tekstu do pliku z metody.")