groceries = {

}

while (True):
    try:
        item = input("")
    except EOFError:
        break
    item = item.lower()
    if item in groceries:
        groceries[item] += 1
    else:
        groceries[item] = 1

print()

# sorted_groceries = dict(sorted(groceries.items(), key=lambda x:x[1]))
# print(sorted_groceries)
for i in sorted(groceries):
    print(f"{groceries[i]} {i.upper()}")