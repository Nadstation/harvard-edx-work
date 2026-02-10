"""
names = []

for _ in range(3):
    names.append(input("What's your  name? "))
    #print(names[_])
    #print(_)


#print(names)

for name in sorted(names):
    print(f"Hello, {name}")
"""



"""
name = input("What's your name?")
file = open("names.txt", "a")
#file.write(f"{name}\n")
file.write(name + "\n")
"""

#file.close() easy to forget to close. can get files corrupted.
#more pythonic when manipuling files is to do this
#with
#that allows you to specify that, in this context, I want you to open and automatically close some file.



#you say with , you call the function in question, and then you say as and specify the name of the variable that should be assigned the return value of open.
#Then, I am going to indent the line underneath so that the line of code that's writing the name is now in the context of this with statement, which just ensures that,
#automatically, If I had more code in this file down below no longer indented, the file would be automatically closed as soon as line file.write is done executing.
"""
name = input("What's your name?")
with open("names.txt", "a") as file:
    file.write(name + "\n")
"""

"""
with open("names.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        #print("hello ", line, end=(''))
        #OR
        print("hello ", line.rstrip())
        #a little better might actually doing this, .rstrip()
        #to strip off at the end of the line, the actual new line itself so that print is handling the printing of everything, the person's name as well as the new line..
        #But you're stripping off what just an implementation detail in the file.
        #We chose to use new lines in my text file to seperate one name from another.
        #it should be cleaner in terms of design to strip that off and then let print print out what is really just now a name.
        #But that's ultimately a design decision. Effect will be exactly the same.

"""






names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

#Very common technique when dealing with files and information more generally, if you want to change that data in some way,
#like sorting it, creating some kind of variable at the top of your program, like a list, adding or appending information to it just to collect it one place
#and then do something interesting with that collection, that list, is exactly what I have done here.
#Let's assume we will continue to accumulate all of the names first into a list,maybe do something to them, maybe forcing them to uppercase or lowercase or the like and then
#and then sort and print out each item.

#Reverse sorted (Z TO A)
#https://docs.python.org/3/library/functions.html#sorted
#sorted(iterable, /, *, key=None, reverse=False)



"""
#if you want to just sort the file.
#can do even more simply with python, particularly by not bothering with this "names" list, not the second "for loop"

with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")

"""

#Csv stands for comma-seperated value
#CSV files very commonly used when you use something like Microsoft Excel, Apple Numbers or Google spreadsheet, and you want to export the data to share to someone else as CSV file.
#Or if you want to import a csv file into your prefered spreadsheet software, like E, N or GS, you can do that as well.

