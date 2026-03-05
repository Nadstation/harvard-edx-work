import sys
import random
from pyfiglet import Figlet


figlet = Figlet()

def main():

    fonts = figlet.getFonts()

    if len(sys.argv) == 3:
        match sys.argv[1]:
            case "-f" | "--font":
                if sys.argv[2] in fonts:
                    entry = input("Input: ")
                    figlet.setFont(font=sys.argv[2])
                    print(figlet.renderText(entry))
                else:
                    raise SystemExit('Invalid usage')

            case _:
                raise SystemExit('Invalid usage')

    elif len(sys.argv) == 1:
        entry = input("Input: ")
        pick = random.choice(fonts)
        figlet.setFont(font=pick)
        print(figlet.renderText(entry))

    else:
        raise SystemExit('Invalid usage')












    #print(f"output: {text_to_emoji(entry)}")

    #print(figlet.getFonts())

    #figlet.setFont(font=f)

    #print(figlet.renderText(entry))






main()
