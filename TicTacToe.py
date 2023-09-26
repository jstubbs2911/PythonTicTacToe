def player_o(board):
    #done = False
    while True:
        x = int(input("Player O,enter 1-9 to select an open position:"))
        if x < 1 or x > 9:
            print("Select a number 1-9 only.\n")
            continue
        elif x == 1:
            if board[0][0] == 1:
                board[0][0] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 2:
            if board[0][1] == 2:
                board[0][1] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 3:
            if board[0][2] == 3:
                board[0][2] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 4:
            if board[1][0] == 4:
                board[1][0] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 5:
            if board[1][1] == 5:
                board[1][1] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 6:
            if board[1][2] == 6:
                board[1][2] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 7:
            if board[2][0] == 7:
                board[2][0] = "O"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 8:
            if board[2][1] == 8:
                board[2][1] = "O"
                break
            else:
                print("This position is already taken")
                continue
        else:
            if board[2][2] == 9:
                board[2][2] = "O"
                break
            else:
                print("This position is already taken")
                continue
    return board
def player_x(board):

    while True:
        x = int(input("Player X,enter 1-9 to select an open position:"))
        if x < 1 or x > 9:
            print("Select a number 1-9 only.\n")
            continue
        elif x == 1:
            if board[0][0] == 1:
                board[0][0] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 2:
            if board[0][1] == 2:
                board[0][1] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 3:
            if board[0][2] == 3:
                board[0][2] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 4:
            if board[1][0] == 4:
                board[1][0] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 5:
            if board[1][1] == 5:
                board[1][1] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 6:
            if board[1][2] == 6:
                board[1][2] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 7:
            if board[2][0] == 7:
                board[2][0] = "X"
                break
            else:
                print("This position is already taken")
                continue
        elif x == 8:
            if board[2][1] == 8:
                board[2][1] = "X"
                break
            else:
                print("This position is already taken")
                continue
        else:
            if board[2][2] == 9:
                board[2][2] = "X"
                break
            else:
                print("This position is already taken")
                continue
    return board
def board_is_full(board):
    count = 0
    for i in board:
        if i[0] == "X" or i[0] == "O":
            count += 1
        if i[1] == "X" or i[1] == "O":
            count += 1
        if i[2] == "X" or i[2] == "O":
            count += 1
    if count == 9:
        return True
    else:
        return False
def check_winner(board):
    XWin = ["X", "X", "X"]
    OWin = ["O", "O", "O"]
    primaryDiagonal = [board[0][0], board[1][1], board[2][2]]
    secondaryDiagonal = [board[0][2], board[1][1], board[2][0]]
    row1 = [board[0][0], board[0][1], board[0][2]]
    row2 = [board[1][0], board[1][1], board[1][2]]
    row3 = [board[2][0], board[2][1], board[2][2]]
    col1 = [board[0][0], board[1][0], board[2][0]]
    col2 = [board[0][1], board[1][1], board[2][1]]
    col3 = [board[0][2], board[1][2], board[2][2]]

    if row1 == XWin:
        return "X"
    elif row2 == XWin:
        return "X"
    elif row3 == XWin:
        return "X"
    elif primaryDiagonal == XWin:
        return "X"
    elif secondaryDiagonal == XWin:
        return "X"
    elif row1 == OWin:
        return "O"
    elif row2 == OWin:
        return "O"
    elif row3 == OWin:
        return "O"
    elif primaryDiagonal == OWin:
        return "O"
    elif secondaryDiagonal == OWin:
        return "O"
    elif board_is_full(board) == True:
        return "Draw"
    if col1 == XWin:
        return "X"
    elif col2 == XWin:
        return "X"
    elif col3 == XWin:
        return "X"
    elif col1 == OWin:
        return "O"
    elif col2 == OWin:
        return "O"
    elif col3 == OWin:
        return "O"
    else:
        return "Continue"
def play_again():
    play = input("Do you want to play again (Y/N)")
    play = play.upper()
    if play == "Y":
        return play
    elif play == "N":
        return play
    else:
        play_again()
def print_board(board):
    print(f"{board[0][0]}  | {board[0][1]} | {board[0][2]}")
    print(f"---+---+---")
    print(f"{board[1][0]}  | {board[1][1]} | {board[1][2]}")
    print(f"---+---+---")
    print(f"{board[2][0]}  | {board[2][1]} | {board[2][2]}")

board = [[1,2,3],[4,5,6],[7,8,9]]
print_board(board)

while True:
    board = player_x(board)
    check = check_winner(board)
    if check == "X":
        print("X won!")
        print_board(board)
        play = play_again()
        if play == "Y":
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print_board(board)
            continue
        else:
            print("Goodbye")
            break
    elif check == "Draw":
        print("Draw! No one wins.")
        print_board(board)
        play = play_again()
        if play == "Y":
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print_board(board)
            continue
        else:
            print("Goodbye")
            break
    else:
        print_board(board)

    ###Player O's Turn if X did not win already and board is not full.
    board = player_o(board)
    check = check_winner(board)
    if check == "O":
        print("O won!")
        print_board(board)
        play = play_again()
        if play == "Y":
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print_board(board)
            continue
        else:
            print("Goodbye")
            break
    elif check == "Draw":
        print("Draw! No one wins.")
        print_board(board)
        play = play_again()
        if play == "Y":
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print_board(board)
            continue
        else:
            print("Goodbye")
            break
    else:
        print_board(board)