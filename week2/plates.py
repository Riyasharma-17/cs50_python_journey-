#Vanity Plates

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Length check
    if len(s) < 2 or len(s) > 6:
        return False

    # First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_started = False

    for char in s:

        # No punctuation or spaces
        if not char.isalnum():
            return False

        if char.isdigit():

            # First number cannot be 0
            if not number_started:
                if char == "0":
                    return False

                number_started = True

        else:
            # No letters after numbers start
            if number_started:
                return False

    return True


main()