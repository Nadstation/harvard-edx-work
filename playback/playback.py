#word = str(input())
#word = word.upper()
#print(word)

def main():
    play = str(input())
    print(slow(play))


def slow(play):
    return play.replace(' ', '...')


main()
