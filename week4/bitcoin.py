# Bitcoin Price Index — Python Project

# This program calculates the current cost of Bitcoin in USD ₿💵

# The user gives the number of Bitcoins through the command line, and the program gets the latest Bitcoin price from an online API.

# Task

# Create a Python file called bitcoin.py that:

# Takes number of Bitcoins from command-line argument
# Gets current Bitcoin price using an API
# Calculates total cost
# Prints result with:
# commas as thousands separators
# 4 decimal places
# Shows error message if input is invalid
# Example
# python bitcoin.py 2

# Output:

# 168,000.1234
# Code
# bitcoin.py

import sys
import requests

try:

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    bitcoins = float(sys.argv[1])

    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey"
    )

    data = response.json()

    price = float(data["data"]["priceUsd"])

    total = bitcoins * price

    print(f"{total:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("Request failed")