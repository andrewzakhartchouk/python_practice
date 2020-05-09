import random

# Cows and Bulls
# A game of Cows and Bulls

print("|| Welcome to Cow and Bulls! I have a 4-digit number and you have to guess it."
      "\nFor every correct number in the correct position, you get a cow,"
      "\nbut correct numbers in the wrong position equate to bulls. ||")


if __name__ == "__main__":
    rnum = str(random.randint(1000, 9999))
    print(rnum)
    guess = 0
    while True:
        pnum = str(input("Guess the 4-digit number (0000 - 9999): "))
        cowbull = [0, 0]
        for i in range(4):
            if rnum[i] == pnum[i]:
                cowbull[0] += 1
            elif pnum[i] in rnum:
                cowbull[1] += 1
        guess += 1
        if cowbull[0] == 4:
            print("          You got all 4 digits in", guess, "guesses!")
            break
        else:
            print("                 You got", cowbull[0], "cows and", cowbull[1], "bulls!")
