first_list = ["Krzysztof","Andrzej","Leopold","Samuel","Robert"]
# sortowanie listy alfabetycznie
first_list.sort()
print(first_list)

# przypisanie elementów z listy do zmiennych
andrzej,krzysztof,leopold,robert,samuel = first_list
print(andrzej)
print(krzysztof)
print(leopold)
print(robert)
print(samuel)

# jeśli nie chcemy zmieniać listy a tylko posortować ją w metodzie
second_list = ["Krystyna", "Aleksandra", "Tamara", "Paulina", "Stanisława"]
sorted_second_list = sorted(second_list)
print(f"Bez sortowania \n{second_list}")
print(f"Posortowana lista metodą sorted() : \n{sorted_second_list}")

# jeśli chcemy posortować listę odwrotnie
reverse_sorted_second_list = sorted(second_list,reverse=True)
print(f"Posortowana lista metodą sorted() z argumentem reverse=True : \n{reverse_sorted_second_list}")

