# Coke Machine 

# A Coke bottle costs 50 cents 🥤
# The machine only accepts these coins:

# 25 cents
# 10 cents
# 5 cents
# Task

# Create a Python file called coke.py that:

# Starts with 50 cents due
# Asks the user to insert coins one by one
# Accepts only 25, 10, or 5
# Ignores any other number
# When total amount reaches 50 or more:
# Print the remaining change
# Example
# Amount Due: 50
# Insert Coin: 25

# Amount Due: 25
# Insert Coin: 25

# Change Owed: 0

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin

change = abs(amount_due)

print(f"Change Owed: {change}")