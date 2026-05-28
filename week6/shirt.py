import sys
from PIL import Image, ImageOps

# Check command-line arguments
if len(sys.argv) != 3:
    sys.exit("Invalid number of command-line arguments")

# Allowed extensions
valid_extensions = [".jpg", ".jpeg", ".png"]

# Get filenames
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check extensions
if not input_file.lower().endswith(tuple(valid_extensions)):
    sys.exit("Invalid input")

if not output_file.lower().endswith(tuple(valid_extensions)):
    sys.exit("Invalid output")

# Check same extensions
if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
    sys.exit("Input and output have different extensions")

try:
    # Open input image
    person = Image.open(input_file)

    # Open shirt image
    shirt = Image.open("shirt.png")

    # Resize and crop input image to shirt size
    person = ImageOps.fit(person, shirt.size)

    # Paste shirt on top
    person.paste(shirt, shirt)

    # Save final image
    person.save(output_file)

except FileNotFoundError:
    sys.exit("Input does not exist")