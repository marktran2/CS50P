import requests
import sys
import json


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
else:

    try:
        object = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()
    else:
        object = object.json()
        price = object["bpi"]["USD"]["rate"]
        price = float(price.replace(",", ""))
        price = round(price * amount, 4)
        print(f"${price:,}")
