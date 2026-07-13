import sys
import os
from PIL import Image, ImageOps

try:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        raise ValueError
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        raise ValueError
    elif not all(string.endswith((".jpg","jpeg",".png")) for string in sys.argv[1:]):
        print("Invalid format")
        raise ValueError
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        print("File extensions must match")
        raise ValueError
    else:
        try:
            shirt = Image.open("shirt.png")
            size = shirt.size
            photo = Image.open(sys.argv[1])
            photo_resized = ImageOps.fit(photo, size)
            photo_resized.paste(shirt, shirt)
            photo_resized.save(sys.argv[2])
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
except ValueError:
    sys.exit(1)
