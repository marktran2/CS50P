names = []

while (True):
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

print("\nAdieu, adieu, to ", end="")
count = 0
for name in names:
    if (count == len(names) - 1):
        print(f"and {name}")
    else:
        print(f"{name}, ", sep="", end="")
    count += 1