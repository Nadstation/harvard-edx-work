def main():
    word = str(input())
    print(convert(word))


def convert(word):
    isSmilesExist = word.find(":)")
    if isSmilesExist >= 0:
        word = word.replace(":)", "\U0001F642")

    isFrownExist = word.find(":(")
    if isFrownExist >= 0:
        word = word.replace(":(", "\U0001F641")

    return word





main()


