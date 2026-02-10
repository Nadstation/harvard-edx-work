"""
try:
    x = int(input("What's X?"))
except ValueError:
    print("X is not an integer")
else:
    print(f"X is {x}")
"""


#Both below worked the same
"""
while True:

    try:
        x = int(input("What's X?"))
    except ValueError:
        print("X is not an integer")
    else:
        break

print(f"X is {x}")


"""
"""

while True:
    try:
        x = int(input("What's X?"))
        break
    except ValueError:
        print("X is not an integer")
    #else:
        #print(f"X is {x}")
        #break

print(f"X is {x}")

"""

def main():
    x = get_int("Hey Bro, what's x?")
    print(f"X is {x}")

    """

def get_int():

    while True:
        try:
            x = int(input("What's X?"))
        except ValueError:
            print("X is not an integer")
        else:
            return x
            #I don't strictly speaking need to write the code as long.
            #Here you could just return x
            #In my else I could break out and return a value
            #So here too, return is used to return values from functions.
            #Break is used to break out of loops.
            #But it turns out that return is sort of stronger than break.
            #It will not only break you out of a loop, it will also return a value for you.
            #So it's doing 2 things for once, if you will.

            #break

    #return x

    """

    #OR

def get_int(prompt):

    while True:
        try:
            return int(input(prompt))
            #I don't have to presumptuously say, what's x?
            #Because what if the program, the caller, wants to ask for Y or Z or some other variable?
            #I can just pass to input whatever prompt the caller has provided.
            #So now I make it more reusable code
            #it's still work just the same, just more reusable. More dynamic.
            #get in doesn't have to know ot care what variable's being asked for, what's being asked for.
            #It just needs to know what prompt it should show to the user.
            # raise You can even raise excpetions yourself , more later.
        except ValueError:
            #print("X is not an integer")
            pass


main()

#it will be nice if the caller main() doesn't have to know what the callee is naming it's variable and vice versa.
#So caller to call a function means to use it. The caller is the function that's using it. The callee is just the function being called.
#It would be nice  if I'm not just hoping that x is the same in both places.
