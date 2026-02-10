def main():
    greeting = input("Greeting: ").lstrip().lower()

    if isGreetingStartWithHello(greeting) == True:
        print("$0")
    elif isGreetingStartWithH(greeting) == True:
        print("$20")
    else:
        print("$100")



def isGreetingStartWithH(greeting):
    i = greeting.find('h')
    if i == 0:
        return True
    else:
        return False

def isGreetingStartWithHello(greeting):
    i = greeting.find('hello', 0, 5)
    if i == 0:
        return True
    else:
        return False


main()




