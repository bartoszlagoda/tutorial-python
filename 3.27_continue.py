index = 0

while index < 5:       # wykonuj instrukcję aż indeks dojdzie do 4
    print(index)        # drukuj na ekranie index
    index = index + 1   # zwiększaj index o 1
    if index == 2:
        continue        # przerywa wszystko co po tej instrukcji i idzie w pętli dalej
    print('Po if')
