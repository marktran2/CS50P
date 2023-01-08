import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if res := re.search(r"([0-9]+)(:[0-9]{2})? ([AP])M to ([0-9]+)(:[0-9]{2})? ([AP])M", s):

        # print(res.group(1))
        # print(res.group(2))
        # print(res.group(3))
        # print(res.group(4))
        # print(res.group(5))

        hour1 = int(res.group(1))
        if res.group(2) == None:
            min1 = 0
        else:
            min1 = int(res.group(2).replace(":", ""))
        status1 = res.group(3)

        hour2 = int(res.group(4))
        if res.group(5) == None:
            min2 = 0
        else:
            min2 = int(res.group(5).replace(":", ""))
        status2 = res.group(6)


        if min1 < 0 or min1 > 59 or min2 < 0 or min2 > 59:
            sys.exit("ValueError")
        elif hour1 < 0 or hour1 > 12 or hour2 < 0 or hour2 > 12:
            sys.exit("ValueError")
        if status1 == "A" and hour1 == 12:
            hour1 = 0
        elif status1 == "P" and hour1 < 12:
            hour1 += 12
        if status2 == "A" and hour2 == 12:
            hour2 = 0
        elif status2 == "P" and hour2 < 12:
            hour2 += 12

        return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"
    else:
        sys.exit("ValueError")


if __name__ == "__main__":
    main()