name = input("What's is the Answer to the Great Question of Life, The Universe, And Eververse, and Everything? ").strip().lower()

"""
if name == "42":
    print("Yes")
elif name == "forty-two":
    print("Yes")
elif name == "forty two":
    print("Yes")
else:
    print("No")
"""

match name:
    case "42" | "forty-two" | "forty two" :
        print("Yes")
    case _:
        print("No")



