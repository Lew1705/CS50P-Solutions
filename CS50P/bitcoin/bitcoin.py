import sys
import requests
from decimal import Decimal, InvalidOperation

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = Decimal(sys.argv[1])
    except InvalidOperation:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https")
        response.raise_for_status()
        data = response.json()
        price = Decimal(str(data["bpi"]["USD"]["rate_float"]))
    except requests.RequestException:
        sys.exit("Network error")

    total = bitcoins * price
    print(f"${total:,.4f}")

main()
