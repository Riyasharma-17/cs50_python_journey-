from datetime import date
from num2words import num2words
import sys


def get_minutes(birthday):
    birth_date = date.fromisoformat(birthday)
    today = date.today()

    days = (today - birth_date).days

    return days * 24 * 60


def convert(minutes):
    return num2words(minutes).replace(" and", "").capitalize()


def main():
    try:
        birthday = input("Date of Birth: ")
        minutes = get_minutes(birthday)
        print(convert(minutes) + " minutes")
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()