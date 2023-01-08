str = input("Input: ")

for char in str:
    c = char.lower()
    if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u':
        print(char, end="")

print()