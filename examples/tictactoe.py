from random import randrange

sign = "A"
def main():
    board = [[i for i in range(1, 4)] for j in range(1, 4)]
    t = 0
    # przyporządkowanie początkowych wartości planszy
    for row in range(0, 3):
        for column in range(0, 3):
            t += 1
            board[row][column] = t

    print("Gra KÓŁKO i KRZYŻYK\n")
    while victory_for(board) == "A":
        draw_move(board)
        if victory_for(board) != "A":
            break
        enter_move(board)


def display_board(board):
    # Funkcja, ktora przyjmuje jeden parametr zawierajacy biezacy stan tablicy
    # i wyswietla go w oknie konsoli.
    for i in range(0, 3):
        j = 0
        print("+-------" * 3 + "+")
        print("|\t\t" * 4)
        print("|", board[i][j], "|", board[i][j + 1], "|", \
              board[i][j + 2], "|", sep="   ")
        print("|\t\t" * 4)
        if i == 2:
            print("+-------" * 3 + "+")
    make_list_of_free_fields(board)



def enter_move(board):
    # Funkcja, ktora przyjmuje parametr odzwierciedlajacy biezacy stan tablicy,
    # prosi uzytkownika o wykonanie ruchu,
    # sprawdza dane wejsciowe i aktualizuje tablice zgodnie z decyzja uzytkownika.
    a = True
    while a:
        userInput = int(input("Wykonaj swój ruch: "))
        if userInput < 1 or userInput > 9:
            print("Niepoprawna wartość.")
            continue
        elif userInput == 1:
            if board[0][0] != 1:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[0][0] = "O"
                a = False
        elif userInput == 2:
            if board[0][1] != 2:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[0][1] = "O"
                a = False
        elif userInput == 3:
            if board[0][2] != 3:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[0][2] = "O"
                a = False
        elif userInput == 4:
            if board[1][0] != 4:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[1][0] = "O"
                a = False
        elif userInput == 5:
            if board[1][1] != 5:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[1][1] = "O"
                a = False
        elif userInput == 6:
            if board[1][2] != 6:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[1][2] = "O"
                a = False
        elif userInput == 7:
            if board[2][0] != 7:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[2][0] = "O"
                a = False
        elif userInput == 8:
            if board[2][1] != 8:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[2][1] = "O"
                a = False
        elif userInput == 9:
            if board[2][2] != 9:
                print("Zajęte. Wybierz inne pole.")
                continue
            else:
                board[2][2] = "O"
                a = False
    return display_board(board)



def make_list_of_free_fields(board):
    notApproval = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "X":
                continue
            elif board[i][j] == "O":
                continue
            else:
                notApproval.append((i,j))
    if not notApproval:
        return True
    else:
        return False



def victory_for(board):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                sign = "X"
                print("Przegrana")
                return sign
            elif board[i][0] == "O":
                sign = "O"
                print("Wygrana")
                return sign
    for i in range(0,3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                sign = "X"
                print("Przegrana")
                return sign
            elif board[0][i] == "O":
                sign = "O"
                print("Wygrana")
                return sign
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            sign = "X"
            print("Przegrana")
            return sign
        elif board[0][0] == "O":
            sign = "O"
            print("Wygrana")
            return sign
    elif board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == "X":
            sign = "X"
            print("Przegrana")
            return sign
        elif board[2][0] == "O":
            sign = "O"
            print("Wygrana")
            return sign
    elif make_list_of_free_fields(board) == True:
        sign = "R"
        print("Remis")
        return sign
    else:
        sign = "A"
        return sign


def draw_move(board):
    a = True
    while a:
        computerInput = randrange(1,9)
        if computerInput == 1:
            if board[0][0] != 1:
                continue
            else:
                board[0][0] = "X"
                a = False
        elif computerInput == 2:
            if board[0][1] != 2:
                continue
            else:
                board[0][1] = "X"
                a = False
        elif computerInput == 3:
            if board[0][2] != 3:
                continue
            else:
                board[0][2] = "X"
                a = False
        elif computerInput == 4:
            if board[1][0] != 4:
                continue
            else:
                board[1][0] = "X"
                a = False
        elif computerInput == 5:
            if board[1][1] != 5:
                continue
            else:
                board[1][1] = "X"
                a = False
        elif computerInput == 6:
            if board[1][2] != 6:
                continue
            else:
                board[1][2] = "X"
                a = False
        elif computerInput == 7:
            if board[2][0] != 7:
                continue
            else:
                board[2][0] = "X"
                a = False
        elif computerInput == 8:
            if board[2][1] != 8:
                continue
            else:
                board[2][1] = "X"
                a = False
        elif computerInput == 9:
            if board[2][2] != 9:
                continue
            else:
                board[2][2] = "X"
                a = False
    return display_board(board)

if __name__ == '__main__':
    main()