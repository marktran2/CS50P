import pyfiglet
import sys


if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    try:
        f = pyfiglet.Figlet(font=sys.argv[2])
    except pyfiglet.FontNotFound:
        sys.exit("Invalid usage")
else:
    f = pyfiglet.Figlet()

phrase = input("Input: ")
print("Output:\n", f.renderText(phrase))