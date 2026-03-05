#https://cs50.harvard.edu/python/psets/0/playback/

def main():
    play = str(input())
    print(slow(play))


def slow(play):
    return play.replace(' ', '...')


main()
