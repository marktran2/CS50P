import sys

def main():
    amount = input("Amount: ")
    fuel = convert(amount)
    if fuel == "ValueError" or fuel == "ZeroDivisionError":
        sys.exit(fuel)
    print(gauge(fuel))


def convert(fraction):
    numerator, denominator = fraction.split(sep="/")
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        return "ValueError"
    
    try:
        num = int(numerator/denominator * 100)
    except ZeroDivisionError:
        return "ZeroDivisionError"

    if numerator > denominator:
        return "ValueError"

    return num

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()