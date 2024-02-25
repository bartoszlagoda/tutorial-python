# RETURN - umożliwia zwracanie wartości z metody

def add(first_num, second_num):
    return first_num + second_num


suma = add(2,2)
print(f"Dodawanie : 2 + 2 \n==================\nWynik: {suma}")
print(f"Dodawanie : 2 + 2 oraz 1 + 1\n=============================\nWynik: {add(2,2) + add(1,1)}")