months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while (True):
    date = input("Date: ")
    date = date.strip()

    if (date[0].isdigit()):
        month, day, year = date.split(sep="/")
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        else:
            if day <= 31 and month <= 12:
                break
    else:
        month, day, year = date.split(sep=" ")
        day = day.replace(",", "")
        try:
            month = months.index(month) + 1
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        else:
            if day <= 31 and month <= 12:
                break

print(f"{year}-{month:02}-{day:02}")