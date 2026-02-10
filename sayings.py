def main():
    hello("World")
    goodbye("World")



def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#It turns out that this variable is a special symbol in Python, __name__
#This is a special variable whose value is automatically set by Python to be __main__ when you run a file from the command line as by running Python of sayings.py
#when you call say.py which does "from sayings  import hello", __name__ equal to "sayings"

if __name__ == "__main__":
    main()
    #print(__name__)


