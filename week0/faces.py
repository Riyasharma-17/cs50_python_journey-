# Making Faces — Python Project

# Before emojis existed, people used text faces like :) and :(
# This program converts those emoticons into real emojis ✨

# Task

# Create a Python file called faces.py that:

# Takes text input from the user
# Changes :) into 🙂
# Changes :( into 🙁
# Keeps all other text unchanged

# Example
# Input:  Hello :)
# Output: Hello 🙂

# Code

def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji


def main():
    greeting = input("Hows your day going? ")
    print(convert(greeting))


main()