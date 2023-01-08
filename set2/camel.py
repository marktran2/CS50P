name = input("camelCase: ")

for i in name:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")

print()