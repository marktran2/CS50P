import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
for line in file:
    if line.startswith("#") == True or line == "\n" or line.lstrip() == "":
        continue
    else:
        print(line, end="")
        count += 1

file.close()

print(count)