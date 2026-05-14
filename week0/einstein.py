# Einstein — Python Project

# Einstein’s famous formula says that mass can be converted into energy ⚡

# E=mc
# 2

# E → Energy (Joules)
# m → Mass (kilograms)
# c → Speed of light (300000000 m/s)
# Task

# Create a Python file called einstein.py that:

# Takes mass as input from the user
# Uses the formula E = mc²
# Prints the energy value as an integer

# Example
# Input: 1
# Output: 90000000000000000

# Code
# einstein.py

m = int(input("Mass: "))

c = 300000000

E = m * c ** 2

print(E)