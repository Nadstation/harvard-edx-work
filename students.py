"""
name,home,house
Harry,"Number Four, Privet Drive",Gryffindor
Ron,The Burrow,Gryffindor
Draco,Malfoy Manor,Slytherin
"""





#Csv stands for comma-seperated value
#CSV files very commonly used when you use something like Microsoft Excel, Apple Numbers or Google spreadsheet, and you want to export the data to share to someone else as CSV file.
#Or if you want to import a csv file into your prefered spreadsheet software, like E, N or GS, you can do that as well.

import csv
#https://docs.python.org/3/library/csv.html
"""
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
"""

"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

"""

"""

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

"""

students = []


with open("students.csv") as file:
    """
    for line in file:
        name, home = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["house"] = house

        student = {"name": name, "home": home}
        students.append(student)
    """
    #changing approach
    #reader = csv.reader(file)
    reader = csv.DictReader(file)



    for row in reader:
        #students.append({"name": row[0], "home":row[1]})
        #Or but more lines
        #print(row)
        """
        name = row[0]
        home = row[1]
        student = {"name": name, "home": home}
        students.append(student)
        """
        students.append(row) #DictReader

        #or Better
        #for name, home in reader:
        #students.append({"name": name, "home": home})
print(students)
print()



def get_name(students):
    #print(students[0]["name"])
    #print(student[])
    return(students["name"])
#get_name(students)

#f = lambda student: student["name"]
#print(f(student))

def get_home(student):
    return student["home"]


#students = sorted(students, key=get_name)

#print(students)


#for student in sorted(students, key=get_name, reverse=False):
for student in sorted(students, key=lambda students: students["name"], reverse=False): #sorting a list of disctionaries with key (name and home) and values here
    #When you pass in a function like get_name or get_house to the sorted function as the value of key,
    #That function is automatically called by the sorted function for you on each of the dictionaries in the list.
    #And is uses the return value of get_name and get_house to decide what strings to actually use to compare in order to decide which is alphabetically correct.
    #So this function, which you pass just by name, you do not pass parentheses at the end, is called by the sorted function to figure out for you how to compare these name values.

    #lambda explenation:
    #I don't use def , I use lambda which says, hey python here comes a function but it has no name, it's anonymous.
    #That function takes a paramater, I could have called anything I want, Students here, Why because this function that's passed in as key is called on every one of the students in that lest
    #every one of the dictionaries in that list.
    #What do I want the anonymous function to return, well given a student I want index into that dictionary and access their name so Hermione, harry and Rone and Draco  is ultimately returned.
    #And that what's the sorted function use to decide how to sort this bigger dictionaries that have other keys, like house as well.
    print(f"{student['name']} is from {student['home']} living in the house {student['house']}")

    #What happens to be clear is that the sorted function will use the value of key get_name,
    #in this case calling that function on every dictionary list that it's supposed to sort.
    #And that function get_name return a string that sorted will actually use to decide whether things go in this order, left-right, or in this order, right-left.
    #it Alphabetizes these things based on that return value.



#print(students)


#print(students)


