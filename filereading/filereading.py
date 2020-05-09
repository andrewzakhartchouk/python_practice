# Read From File
# Reading two files into dictionaries


lister = {}
with open("nameslist.txt", "r") as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in lister:
            lister[line] += 1
        else:
            lister[line] = 1
        line = f.readline()

print(lister)

category_dict = {}
with open("Training_01.txt") as f:
    categories = [line.split("/")[2] for line in f]
    for item in categories:
        if item in category_dict:
            category_dict[item] += 1
        else:
            category_dict[item] = 1

print(category_dict)


# File Overlap
# Checks overlap of two files


def read_in_numlist(textfilename):
    with open(textfilename) as f:
        return [line.split("\n")[0] for line in f]


plist = read_in_numlist("primenumbers.txt")
hlist = read_in_numlist("happynumbers.txt")

olist = [int(i) for i in plist if i in hlist]
print(olist)
