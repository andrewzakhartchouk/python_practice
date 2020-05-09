import random

# Hangman
# A game where you guess the word, one letter at a time


def text_read(textfile):
    with open(textfile) as f:
        return [line.split("\n")[0] for line in f]


def chooseword(sowpodlist):
    a = random.choice(sowpodlist)
    return [len(a), a]


def take_guess():
    return input("Guess a letter: ").upper()


def display(length, hword):
    board = list("_") * length
    attempt = round(length * 1.5)
    guessed_words = []
    while attempt > 0:
        print(" ".join(board))
        g = take_guess().strip()
        if g not in guessed_words:
            guessed_words.append(g)
            attempt -= 1
            for i in range(length):
                if g in hword[i]:
                    board[i] = g
            if "_" not in board:
                print(" ".join(board))
                print("Congratulations, you got it!")
                exit()
            print("You have", attempt, "guesses left.")
        else:
            print("Try again")
    print("You have run out of guesses. Bad luck!"
          "\nThe word was:", "".join(hword))


if __name__ == "__main__":
    print("Welcome to Hangman!")
    stuff = chooseword(text_read("sowpods.txt"))
    wordlen = stuff[0]
    word = list(stuff[1])
    display(wordlen, word)
