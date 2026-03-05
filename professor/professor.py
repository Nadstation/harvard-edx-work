#https://cs50.harvard.edu/python/psets/4/professor/

from random import randint


def main():

    while(True):
        level = get_level()
        match level:
            case 1 | 2 | 3 :
                print("ok")
                x   = generate_integer(level)
                y   = generate_integer(level)
                answer = input(f"{x} + {y} = ")
                print (answer)
            case _:
                pass

def get_level():
    level = int(input("Level: "))
    return level


def generate_integer(level):
    int   = randint(0, 9)
    return int



if __name__ == "__main__":
    main()
