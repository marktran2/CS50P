import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    file1 = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
else:
    file2 = open(sys.argv[2], "w")
    reader = csv.reader(file1)
    file2.write("first, last, house\n")
    count = 0
    for name, house in reader:
        if count == 0:
            count += 1
            continue
        # print(f"{name} is in {house}")
        last, first = name.split(sep=",")
        file2.write(f"{first.lstrip()}, {last.lstrip()}, {house.lstrip()}\n")



file2.close()
file1.close()