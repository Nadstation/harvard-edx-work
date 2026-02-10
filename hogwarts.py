students = ["Hermione", "Harry", "Ron"]
#print(students[0]) #0 indexed, The first item in the list is at location 0. The second is at location 1 etc..

#print(students[1])
#print(students[2])


#You don't need to manually initiaze Student, Python takes care of initializing the student variable to Hermione first then Harry second, then Ron third.
#Unlike other languages, You don't need to initialize it to something yourself. It just exists and it will work.
#for student in students:
#    print(student)

#for i in range(len(students)):
#    print(i+1 , students[i])


"""
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")
"""


students = [                                                            # A list
    {"name" : "Hermione", "house": "Gryffindor", "patronus": "Otter"},  # A dictionary,  a collection of key value pairs. How many keys does this first dictionary have? another way, How many words are in that dictionary? Three, the words are name, house and patronus. What are the definitions of values of those words in Hermione's dictionary? Hermione, Gryffindor and Otter.
    {"name" : "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name" : "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name" : "Draco", "house": "Slytherin", "patronus": None}
    ]

for student in students:
   print(student["name"], student["house"], student["patronus"],sep=", ")


""" My own test
for i in range(len(students)):
   ##print(i+1 , students[i])
   if i == 0:
      print(i+1, students[0]["name"], students[0]["house"], sep=", ")
"""


