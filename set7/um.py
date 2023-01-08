import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.strip()

    um_count =  re.findall(r"\bum\b", s, re.IGNORECASE)

    return len(um_count)

if __name__ == "__main__":
    main()