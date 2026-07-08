import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    randomfont = choice(fonts)
    figlet.setFont(font=randomfont)
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1]!= "--font":
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        figlet.setFont(font=sys.argv[2])
        print(sys.argv[2])
else:
    sys.exit("Invalid usage")


text = input("Input: ")
print(figlet.renderText(text))





