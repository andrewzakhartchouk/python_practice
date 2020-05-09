# Guessing Game 2
# Computer guesses your number


def guesser():
    lval = 1
    hval = 999
    guess = 500
    counter = 0

    print("Pick a number from 1 to 999 and I'll try to guess it."
          "\nJust tell me if I'm correct, or 'higher'/'lower'.")
    while True:
        counter += 1
        print("Is", guess, "your number?")
        response = input("type: 'yes', 'higher' or 'lower'"
                         "\n= ")
        if response == "yes":
            print("Yay, I got it in", counter, "tries. Thanks for playing!")
            break
        elif response == "higher":
            lval = guess + 1
        elif response == "lower":
            hval = guess - 1

        guess = (hval + lval) // 2

guesser()
