# Outdated 

# Different countries write dates differently 📅
# This program converts dates into standard ISO format:

# YYYY-MM-DD
# Task

# Create a Python file called outdated.py that:

# Takes a date from the user in either format:
# 9/8/1636

# or

# September 8, 1636
# Converts it into:
# 1636-09-08
# Keeps asking again if input is invalid

# Code
# outdated.py

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:

    try:
        date = input("Date: ").strip()

        if "/" in date:

            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        elif "," in date:

            month_day, year = date.split(",")

            month_name, day = month_day.split()

            month = months.index(month_name) + 1

            day = int(day)
            year = int(year)

        else:
            continue

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        pass