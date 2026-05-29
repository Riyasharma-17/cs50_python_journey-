import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    matches = re.match(pattern, s)

    if not matches:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = matches.groups()

    # Default minutes to 00 if missing
    if m1 is None:
        m1 = "00"

    if m2 is None:
        m2 = "00"

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1)
    m2 = int(m2)

    # Validate time
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError

    # Convert first time
    if p1 == "AM":
        if h1 == 12:
            h1 = 0
    else:
        if h1 != 12:
            h1 += 12

    # Convert second time
    if p2 == "AM":
        if h2 == 12:
            h2 = 0
    else:
        if h2 != 12:
            h2 += 12

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()