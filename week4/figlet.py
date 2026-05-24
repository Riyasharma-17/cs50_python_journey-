import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

    if sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

figlet.setFont(font=font)

text = input("Input: ")

print(figlet.renderText(text))