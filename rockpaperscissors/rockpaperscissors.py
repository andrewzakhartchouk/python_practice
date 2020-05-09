# Rock Paper Scissors
# A simple rock paper scissors game with 2 players

choice = ["p", "r", "s"]
while True:
    p1 = input("Player 1: Rock (r) Paper (p) Scissors (s)\n = ").lower()
    p2 = input("Player 2: Rock (r) Paper (p) Scissors (s)\n = ").lower()
    if p1 == p2:
        "Draw!"
    if choice.index(p1) == (choice.index(p2) + 1) % 3:
        print("Player 2 Wins!")
    elif choice.index(p2) == (choice.index(p1) + 1) % 3:
        print("Player 1 Wins!")

    x = input("Play another round? (y/n)\n= ")
    if x == "n":
        break
