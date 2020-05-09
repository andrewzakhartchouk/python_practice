import random

# Password Generator
# Generates a weak/medium/strong password


def passgen(a, b):
    password = []
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "12345678901234567890"
    symbols = "!@#$%^&*!@#$%^&*"
    while len(password) < b:
        if a == 1:
            password.append(random.choice(lowerCase + upperCase))
        elif a == 2:
            password.append(random.choice(lowerCase + upperCase + numbers))
        if a == 3:
            password.append(random.choice(lowerCase + upperCase + numbers + symbols))
    return ''.join(password)


strength = int(input("I am a password generator. Choose your password strength:"
                     "\n|1| Weak: Only letters"
                     "\n|2| Medium: Letters and numbers"
                     "\n|3| Strong: Symbols, letters and numbers"
                     "\nEnter a number: "))
length = int(input("And choose a length (1-24): "))
print(passgen(strength, length))
