"""
print("meow")
print("meow")
print("meow")
"""

"""
i = 3
while i != 0:
    print("meow")
    i = i - 1
"""

"""
i = 0
while i < 3 :
    print("meow")
    #i = i + 1
    i += 1
"""



# The way of loop works is that it allows you to iterate over a list of items.
"""
#each excecution of this loop, I want to print out "meow",
                     #if you want a variable like i , a number, and you know in advance how many times you want this loops to execute -- 3 times,
                     #we will just kind of specify what it is you want i to take on as values explicitly.
                     In this loop, i will be automatically initialized by python to be 0, then meow will be printed.
                     Then Python would automatically update i to equal 1, then meow will be printed. Then...
                     And because that's it for the values in that list. Python will stop.
"""
"""
for i in [0, 1, 50]:
    print("meow")
    print(i)

"""

#for i in range(3): even though I am defining a variable i, I am not ever using it.
#If you need a variable, just because the programming feature requires it to do some kind of counting updating,
#but you, the human don't care about its value, a pythonic improvement here would be to name that variable a single underscore,
#just because it's not required, it doesn't change the correctness of the program, it signals to yourself later that yes it's a variable
#but you don't care about its name because you're not using it later. it's just necessary  in order to use this feature, this loop in this case here.

"""
for _ in range(3):
    print("meow")
    #i is a variable , we don't use it, but it's necessary for this programming feature, it requires it to do some kind of counting, or automatic updating.
    #it has to know what it's iterating over.
    #_ more pythonic, it's not required, it doesn't change the correctness of the program, it signals,  yes it is a variable but you don't care about its name because
    #you're not using it later, it 's just necessary in order to use this feature.
"""

#print("meow\n" * 3, end="")

"""
n = int(input("What's n?"))
if n < 0:
    n = int(input("What's n?"))
    if n < 0:
        n = int(input(""))

"""



#This is a very common paradigm in Python when you want to do something again again and again
#but only the user actually gives you a value that you care about here.

#while True:
#    n = int(input("What's n?" ))
    ##if  n < 0:
    ##   continue
    ##else:
    ##    break
#    if n > 0:
#       break

#for _ in range (n):
#   print("meow")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break

    return n



def meow(n):
    for _ in range(n):
        print("meow")

main()











