# twttr.py

def main():

    word = input("Input: ")

    print(shorten(word))


def shorten(word):

    vowels = "AEIOUaeiou"

    result = ""

    for letter in word:

        if letter not in vowels:
            result += letter

    return result


if __name__ == "__main__":
    main()