#pip install requests
#https://itunes.apple.com/search?entity=song&limit=1&term=weezer
#JSON Javascript object notation
#Technically related to another programming language called javascript But Json this day is typically used nowdays as a language agnostic format for exchanging data between computers.
#By language agnostic I mean you don't have to use Javascript. You can use Python or any other language to read JSON or write it as well.
#It's a complete text based format which means that I visit that URL with my browser, what gets downloaded is just a bunch of text.
#But that text is formatted in a standard way using curly braces {} and square brackets [] using quotes and  some colons that ultimately contains all the information  in Apple's database on Weezer's song, at least the forst one because I limited to one in their database.
#And that's an API , an application programming interface, a mechanisme whereby I can access data on someone else server and somehow integrated into my own program.

import json #comes with python , no need to install manually.
import requests
#to make HTTP requests
import sys

if len(sys.argv) != 2:
    sys.exit()

#use the requests library to write some python code that effectively is pretending to be a web browser so as to connect to that same HTTPS URL on Apple's own server
response = requests.get("http://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(response.json())
#print(json.dumps(response.json(), indent=2))

o = response.json()

#print(json.dumps(o, indent=2))


#To print out all of the songs that itunes has for the band weezer, maybe iterates over this somehow
#here is the key called trackName, it is inside of a dictionary that is a value of results here. (1hour:05min)

for result in o["results"]:
    print(result["trackName"])


#What you will see here is that this has been standardized now as a python dictionary.
#Apple's returning is a JSON response but Python, the request library is converting it to a python dictionary.Use almost the same synthax.
#docs.python.org/3/library/json.html
#It turns out that python also comes with a special library called JSON that allows you to manipulate JSON Data and even just pretty printed, that is formatted in a way that's going to be way easier for you and I to understand.

