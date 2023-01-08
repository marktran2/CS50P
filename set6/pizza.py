import csv
import sys
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")


try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

reader = csv.reader(file)

header = []
for row in reader:
    header.append(row)

print(tabulate.tabulate(header, headers=header[0], tablefmt="grid"))

file.close()