# Draw a Game Board
# Drawing a board of any size


def boardgen(size):
    top = " ---"
    side = "|"
    return (top * size + "\n" + ((side + "   ") * size) + side + "\n") * size + (top * size)


gameboard = boardgen(int(input("Choose the size of the playing board: ")))
print(gameboard)


# Check Tic Tac Toe
# Checks win condition for a game of Tic Tac Toe


def checker(m):
    w = 0

    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2] != 0:
            w = m[i][0]
        elif m[0][i] == m[1][i] == m[2][i] != 0:
            w = m[0][i]
        elif m[0][0] == m[1][1] == m[2][2] != 0:
            w = m[0][0]
        elif m[0][2] == m[1][1] == m[2][0] != 0:
            w = m[0][2]

    if w == 1:
        print("Player 1 wins!")
    elif w == 2:
        print("Player 2 wins!")
    else:
        print("No one wins!")


board = [[0, 2, 0],
         [1, 1, 1],
         [0, 0, 0]]

checker(board)


# Tic Tac Toe Draw
# Combining a scoreboard with a visual board


def drawer():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    print("Player 1 is X")
    print("Player 2 is O")
    i = 0
    while True:
        while True:
            p1i = input("Player 1 (X): Type 'row,column': ").split(",")
            hori = int(p1i[0]) - 1
            vert = int(p1i[1]) - 1
            if board[hori][vert] == 0:
                board[hori][vert] = "X"
                break
            else:
                print("Try again.")
                continue
        i += 1
        print(board)
        if i == 9:
            break
        while True:
            p2i = input("Player 2 (O): Type 'row,column': ").split(",")
            hori = int(p2i[0]) - 1
            vert = int(p2i[1]) - 1
            if board[hori][vert] == 0:
                board[hori][vert] = "O"
                break
            else:
                print("Try again.")
                continue
        print(board)
        i += 1


drawer()
