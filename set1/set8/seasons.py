from datetime import date
import re
from num2words import num2words
import sys

def main():
    dob = input("Date of Birth: ")
    print(calculate_time(dob))

        

def calculate_time(dob):
    if res := re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)", dob):
        year = int(res.group(1))
        month = int(res.group(2))
        day = int(res.group(3))
        birth = date(year, month, day)

        now = date.today()

        res = now - birth
        timediff = res.days

        if timediff < 0:
            sys.exit("Invalid date")

        timediff = timediff * 24 * 60

        str = num2words(timediff)

        return f'{str.capitalize().replace("and ", "")} minutes'

    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()