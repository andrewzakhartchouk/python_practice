import random


# Character Input
# A simple character input return the year the person will be 100

name = input("Enter name: ")
age = int(input("Enter age: "))
year = int(input("What year is it?: "))

print(name, "will turn 100 in the year", (year + 100 - age))


# Odd or Even
# Checks if the number is odd or even, and takes a second number to divide by the first.

print("I know if it's odd or even!")

running = True
while running:
    number1 = input("Give me a number (or just say stop): ")
    if number1 == "stop":
        break
    number1 = int(number1)
    if number1 % 2 == 0:
        if number1 % 2 == 0:
            print("This is a multiple of 4, that's cool.")
        else:
            print("This is an even number")
    else:
        print("This is an odd number")

    number2 = int(input("Now give me a number to divide by your first number: "))
    if number2 % number1 == 0:
        print(number2, "÷", number1, "divides cleanly!")
    else:
        print(number2, "÷", number1, "ain't a clean division!")


# List Less Than Ten
# Filters out any numbers larger than the given number.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
b = int(input("Give me a number to reduce the list to anything less than it:\n"))
print([aa for aa in a if aa < b])  # [output] for [item] in [list] if [filter]


# Divisors
# Checks if it is a prime number

a = int(input("Number: "))
aa = list(range(1, a + 1))
bb = [b for b in aa if a % b == 0]
if len(bb) == 1 or 2:
    print("Prime Number!")
print(bb)


# List Overlap
# Generates two random lists and returns the overlap

a = random.sample(range(1, 100), random.randint(1, 20))
print(a)
b = random.sample(range(1, 100), random.randint(1, 20))
print(b)

c = []
for number in a:
    if number in b:
        if number not in c:
            c.append(number)
if len(c) == 0:
    print("No matches")
else:
    print(c)

# List Overlap Comprehensions
# Using a list comprehension

a = random.sample(range(1, 100), random.randint(1, 20))
print(a)
b = random.sample(range(1, 100), random.randint(1, 20))
print(b)

print(list(set([c for c in a if c in b])))


# String Lists
# Checks for a palindrome (word is the same in reverse)

check = input("Palindrome checker: ")
if check == check[::-1]:
    print(check, "is a palindrome!")
else:
    print(check, "is not a palindrome.")

# List Comprehensions
# Practicing list comprehension to return only even numbers

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([aa for aa in a if aa % 2 == 0])

numlist = []  # A random test list generator
list_length = random.randint(5, 15)

while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))


# Check Primality Functions
# Returns all prime numbers between 0 and given number

def get_input(pinput="Give me a number: "):
    return int(input(pinput))


def prime(r):
    return [b for b in range(1, r + 1) if r % b == 0]


a = get_input()
checklist = prime(a)
if len(checklist) <= 2 and a != 1:
    print("That's a prime number!")
else:
    print("That's not a prime number!")


# List Ends
# List selection


def listends(l):
    return [l[0], l[-1]]


a = [5, 10, 15, 20, 25]
print(listends(a))


# Fibonacci
# Returns the Fibonacci sequence for a given length

def fibo(a):
    fibonacci = [1, 1]
    if a == 1:
        fibonacci = [1]
    while len(fibonacci) < a:
        i = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(i)
    return fibonacci


b = int(input("Give me the length of the Fibonacci sequence: "))
print(fibo(b))


# List Remove Duplicates
# Returns a list of no duplicates (set)

a = [1, 1, 1, 2, 2, 3, 35, 212]


def deldupes(dlist):
    return list(set(dlist))


def ldeldupes(dlist):
    b = []
    [b.append(i) for i in dlist if i not in b]
    return b


print(deldupes(a))
print(ldeldupes(a))


# Reverse Word Order
# Reverses a given string


def string(a):
    rstring = " ".join(a.split()[::-1])
    return rstring


print(string(input("Give me a bunch of words to reverse: ")))

# Element Search
# A first try at binary search


def find(target, flist):
    while True:
        mid_ind = int(len(flist) / 2)
        mid_int = flist[mid_ind]
        if mid_int == target:
            return True
        if len(flist) == 1:
            return False
        if mid_int < target:
            flist = flist[mid_ind:]
        else:
            flist = flist[:mid_ind]


if __name__ == "__main__":
    olist = [1, 3, 5, 30, 42, 43, 500]
    number = 31

    print(find(number, olist))

# Max of Three
# Finding the largest of 3 given numbers


def maxfunc(a, b, c):
    if a < b:
        a = c
    else:
        b = c
    if a < b:
        a = b
    return a


print(maxfunc(5, 10, 20), "is the largest of the three.")


