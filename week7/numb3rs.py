import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # Check basic IPv4 pattern
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False

    # Split into parts
    parts = ip.split(".")

    # Check each number
    for part in parts:
        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


if __name__ == "__main__":
    main()