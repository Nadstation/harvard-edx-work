# Ask user for their name
#name = input("What's your name? ")

# Remove whitespace from str and capitalize user's name
#name = name.strip().title() #chain the function together
#We can do one step further
##name = input("What's your name? ").strip().title()

#Split user's name into first name and last name

##first, last = name.split(" ")




# Remove whitespace from str
#name = name.strip() #use a function a little differently, in this context called a method, again = is for assignment for updateing the variable name
#Capitalize user's name just the very first letter
#name = name.capitalize()


#Capitalize user's name not just the very first letter, function called Title that do title-based capitalization, first letter of each word.
#name = name.title()

# Say hello to user

"""
Is a comment
"""

#print("hello,", name)
#When you pass multiple arguments to print, it automatically inserts a space for you.

#OR

"""
print("hello, " + name)
it's the same.

+ means no addition but concatenation of strings

"""


#print("hello, ", end="")
#print(name)

#print("hello,", name, sep='')

#print('hello, "friend"')
#OR
#print("hello, \"friend\"")


#print("hello,", name)
##print(f"hello, {name}") #another way to solve the same problem


"""

https://docs.python.org/3/library/functions.html#print

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

everything inside those parenthesys are the arguments, the potential arguments to the function.
However when we are looking at these arguments in a documentation like this.
There is technically a different term that we would use. These are technically the paramaters to the function.
So when we are talking about what you can pass to a function and what those inputs are called, those are paramaters.
When you actually use the function and pass in values inside those parenthesis, those inputs those values are arguments.

When we are looking at what a function can take vs what you 're actually passing into the function.

\n means new line


"""


"""
https://docs.python.org/3/library/stdtypes.html#string-methods

"""


#function

"""
def hello(to="world"):
    print("hello", to)


hello()
name = input("What's your name? ")
hello(name)

#print(name)
"""

def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    #print("hello", to)
    return f"hello, {to}"


if __name__ == "__main__":
    main()
