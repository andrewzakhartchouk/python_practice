import random

# Guessing Game 1
# Try to guess the number

r = random.randrange(1, 10)
i = 0
print("// I'm thinking of a number between 1 and 9 (type 'exit' to quit). //")
while True:
    g = input("Try to guess: ")
    if g == "exit":
        print("Goodbye!")
        break
    g = int(g)
    i += 1
    if g == r:
        print("You guessed right!")
        print("You guessed", i, "times")
        break
    elif g > r:
        print("Too high!")
    elif g < r:
        print("Too low!")
