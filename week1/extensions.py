# File Extensions 

# Files have extensions like .jpg, .png, .pdf etc.
# These extensions help computers understand the file type 📁

# This program checks a file’s extension and prints its media type.

# Task

# Create a Python file called extensions.py that:

# Takes a file name from the user
# Checks its extension
# Prints the correct media type
# Supported Types
# .gif   → image/gif
# .jpg   → image/jpeg
# .jpeg  → image/jpeg
# .png   → image/png
# .pdf   → application/pdf
# .txt   → text/plain
# .zip   → application/zip
# If the extension is unknown, print:
# application/octet-stream

# Example
# Input: cat.png
# Output: image/png

# Code


file = input("File name: ").lower().strip()

if file.endswith(".gif"):
    print("image/gif")

elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")

elif file.endswith(".png"):
    print("image/png")

elif file.endswith(".pdf"):
    print("application/pdf")

elif file.endswith(".txt"):
    print("text/plain")

elif file.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")