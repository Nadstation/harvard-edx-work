#https://cs50.harvard.edu/python/psets/0/indoor/

def main():
    name = str(input())
    print(voice(name))


def voice(to):
    #print("hello", to)
    return to.lower()

main()
