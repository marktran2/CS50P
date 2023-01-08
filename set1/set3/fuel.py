while (True):
    fuel = input("Fraction: ")

    try:
        numerator, denominator = fuel.split(sep="/")
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        continue
    
    if numerator > denominator:
        continue

    try:
        amount = int((numerator / denominator) * 100)
        break
    except ZeroDivisionError:
        continue

if amount <= 1:
    print("E")
elif amount >= 99:
    print("F")
else:
    print(amount, "%", sep="")