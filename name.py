#docs.python.org/3/library/sys.html
import sys


"""
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""

#check for errors
if   len(sys.argv) < 2 :
    #print("Too few arguments")
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2 :
    #print("Too many arguments")
#   sys.exit("Too many arguments")

for arg in sys.argv[1:]:
    #slices
    #To take a slice of a list means to take a subset of it.
    #You can simply do this.
    #At the end of the list name, sys.argv in this case, you can use square brackets.
    #And then in those  square brackets, you can specify the start and the end of the list that you want to retain.
    #I want to start at the element 1, not 0. And I just want to go to the end. sys.argv[1:]
    print("Hello, my name is", arg)
#




#else:
#    print("Hello, my name is", sys.argv[1])

#print the name tags
##print("Hello, my name is", sys.argv[1])

#The essence of my program which is just to print out the name tag, is relegated to this else clause
#That's fine , logically it's correct but generally speaking , there is something nice about all your error handling seperate from the code that you really care about.
#It would be nice only for design sake not to hide  in this else statement the actual code that you care about.




