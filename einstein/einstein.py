#https://cs50.harvard.edu/python/psets/0/einstein/

c = 300000000

def main():

    mass = int(input("m: "))
    print(energy(mass))

    #print(convert(word))


def energy(m):

    energy = int(m * c * c)

    return f"E: {energy}"




main()
