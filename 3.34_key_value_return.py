# RETURN - umożliwia zwracanie wartości z metody

def add(first_num, second_num):
    return first_num + second_num


def sub(first_num, second_num):
    return first_num - second_num

def sub_with_none(first_num, second_num):
    print(first_num - second_num)
# None - specjalny obiekt, który oznacza obiekt pusty, aby zaznaczyć zmienną jako dostępną ale chwilowo nieokreśloną

suma = add(2,2)
print(f"Dodawanie : 2 + 2 \n==================\nWynik: {suma}")
print(f"Dodawanie : 2 + 2 oraz 1 + 1\n=============================\nWynik: {add(2,2) + add(1,1)}")
print(f"Odejmowanie : 3 - 2 \n==================\nWynik: {sub(3,2)}")
print(f"Odejmowanie dla obiektu None: 3 - 2 \n==========================\nWynik: {sub_with_none(3,2)}")