#Just setting up my twttr
word = input("Which social media platform do you use most? ")

for char in word:
    if char not in "aeiouAEIOU":
        print(char, end="")
