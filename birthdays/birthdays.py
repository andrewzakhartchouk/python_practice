import json
from collections import Counter

# Birthday Dictionaries
# Using dictionaries for birthdays


birthdays = {"Andrew": "1996/06/22", "Bob": "1993/02/01", "Dylan": "1986/11/29", "Jeff": "1969/03/02"}
with open("./birthdaydict.json", "w") as f:
    json.dump(birthdays, f)
print("Welcome, we have a few birthdays saved here.")
for item in birthdays:
    print("  " + item)
name = str(input("Who's birthday would you like to know?: "))
if name in birthdays:
    print("{}'s birthday is {}".format(name, birthdays[name]))
else:
    print("Unfortunately, we do not have {} in our list.".format(name))


# Birthday JSON
# Storing birthdays in a .JSON files

with open("./birthdaydict.json", "r") as f:
    birthdays = json.load(f)

while True:
    choice = input("\nPlease input number for choice:"
                   "\n[1] : Look up a birthday"
                   "\n[2] : Add/edit a birthday"
                   "\n[3] : Save and quit"
                   "\n= ")
    if choice == "1":
        print("We have a few birthdays saved here.")
        for item in birthdays:
            print("    ", item)
        name = input("Who would you like to look up?: ")
        if name in birthdays:
            print("{}'s birthday is {}".format(name, birthdays[name]))
        else:
            print("Unfortunately, we do not have {} in our list.".format(name))
    if choice == "2":
        newname = input("Enter name: ")
        newage = input("Enter birthday (YYYY/MM/DD): ")
        birthdays[str(newname)] = str(newage)
        print("{} and their birthday {} has been added to the list. "
              "Please remember to save and quit.".format(newname, newage))
    if choice == "3":
        print("Saving...")
        with open("./birthdaydict.json", "w") as f:
            json.dump(birthdays, f)
        print("Saved! Come again soon!")
        quit()


# Birthday Months
# Counting the number of people with birthdays in each month


with open("./birthdaydict.json", "r") as f:
    birthdays = json.load(f)
    months = []
num_to_string = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"}

for name in birthdays.keys():
    month = birthdays[name].split("/")[1]
    months.append(num_to_string[month])

print(Counter(months))
