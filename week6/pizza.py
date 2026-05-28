import sys
import csv
from tabulate import tabulate

# Check command-line arguments
if len(sys.argv) != 2:
    sys.exit("Too few or too many command-line arguments")

# Check file extension
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    # Open CSV file
    with open(sys.argv[1]) as file:

        # Read CSV content
        reader = csv.reader(file)

        # Convert all rows into a list
        table = list(reader)

        # Print formatted table
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

# File not found
except FileNotFoundError:
    sys.exit("File does not exist")