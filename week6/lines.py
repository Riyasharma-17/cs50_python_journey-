# lines.py

import sys

if len(sys.argv) != 2:
    sys.exit("Invalid number of command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:

    count = 0

    with open(filename) as file:

        for line in file:

            stripped = line.strip()

            if stripped == "":
                continue

            if stripped.startswith("#"):
                continue

            count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")