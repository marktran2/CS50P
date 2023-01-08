import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        byte_list = ip.split(".")
        for byte in byte_list:
            if int(byte) < 0 or int(byte) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()