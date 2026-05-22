# Felipe's Taqueria

# This program lets a user order food from Felipe’s Taqueria 🌮

# Each time the user enters an item:

# Add its price to the total
# Show the updated bill
# Menu
# Baja Taco         → $4.25
# Burrito           → $7.50
# Bowl              → $8.50
# Nachos            → $11.00
# Quesadilla        → $8.50
# Super Burrito     → $8.50
# Super Quesadilla  → $9.50
# Taco              → $3.00
# Tortilla Salad    → $8.00
# Task

# Create a Python file called taqueria.py that:

# Takes food items from the user one by one
# Ignores uppercase/lowercase differences
# Ignores invalid items
# Shows total price after every valid item
# Stops when user presses Ctrl + D

# Example
# Item: burrito
# Total: $7.50

# Item: taco
# Total: $10.50

# Code

# taqueria.py

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

try:
    while True:

        item = input("Item: ").title()

        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")

except EOFError:
    print()