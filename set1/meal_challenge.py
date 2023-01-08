def main():
    time = input("What time is it? ")
    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    num, relation = time.split(sep=None, maxsplit=1)


    hour, minute = num.split(sep=":", maxsplit=1)
    hour = float(hour)

    if relation == "p.m.":
        hour += 12

    minute = float(minute)
    return hour + (minute / 60)


main()