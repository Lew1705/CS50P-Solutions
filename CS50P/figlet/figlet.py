import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font=font)
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")

    print("Output:")
    print(figlet.renderText(text))

main()
