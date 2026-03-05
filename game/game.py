#https://cs50.harvard.edu/python/psets/4/game/

from random import randint

def main():

    while(True):
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            else:
                new   = randint(1, level)
            while(True):
                try:
                    guess = int(input("Guess: "))
                    if guess <= 0:
                        raise ValueError
                    elif guess > level:
                        print("Too large!")
                    elif guess > new:
                        print("Too large!")
                    elif guess < new:
                        print("too small!")
                    else:
                        print("Just right!")
                        exit()
                except ValueError:
                    pass


        except ValueError:
            pass

main()


