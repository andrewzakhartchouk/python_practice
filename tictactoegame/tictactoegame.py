# Tic Tac Toe
# Full game of Tic Tac Toe


def game():
    i = 0
    running = True
    while running:
        while True:
            p1i = input("Player 1 (X): Type 'row,column': ").split(",")
            hori = int(p1i[0]) - 1
            vert = int(p1i[1]) - 1
            if scoreboard[hori][vert] == 0:
                scoreboard[hori][vert] = "X"
                break
            else:
                print("Try again.")
                continue
        draw_board(scoreboard)
        if checker(scoreboard) == "finish":
            exit()
        i += 1
        if i == 9:
            "No winners"
            exit()
        while True:
            p2i = input("Player 2 (O): Type 'row,column': ").split(",")
            hori = int(p2i[0]) - 1
            vert = int(p2i[1]) - 1
            if scoreboard[hori][vert] == 0:
                scoreboard[hori][vert] = "O"
                break
            else:
                print("Try again.")
                continue
        draw_board(scoreboard)
        if checker(scoreboard) == "finish":
            exit()
        i += 1


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

    if w == "X":
        print("Player 1 wins!")
        return "finish"
    elif w == "O":
        print("Player 2 wins!")
        return "finish"


def draw_board(m):
    print("\n\n\n\n --- --- --- " \
          "\n| " + str(m[0][0]) + " | " + str(m[0][1]) + " | " + str(m[0][2]) + " |" \
                                                                                "\n --- --- --- " \
                                                                                "\n| " + str(
        m[1][0]) + " | " + str(m[1][1]) + " | " + str(m[1][2]) + " |" \
                                                                 "\n --- --- --- " \
                                                                 "\n| " + str(
        m[2][0]) + " | " + str(m[2][1]) + " | " + str(m[2][2]) + " |" \
                                                                 "\n --- --- ---")


scoreboard = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
draw_board(scoreboard)
print("Player 1 is X")
print("Player 2 is O")
while True:
    game()
