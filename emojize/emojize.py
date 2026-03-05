import emoji


def main():

    entry = input("Input: ")
    print(f"output: {text_to_emoji(entry)}")




def text_to_emoji(e):

    x = emoji.emojize(e, language='alias')
    return x




main()
