#x = int(input("What's x? "))
#y = int(input("What's y? "))

#z = int(x) + int(y)
#print(z)

#print(x + y)

#print(int(input("What's x? "))+int(input("What's y? ")))


##x = float(input("What's x? "))
##y = float(input("What's y? "))

#z = round((x + y),2)
#z = round(x + y)
#z = round(x / y,2)
##z = x / y

##print(f"{z:.2f}")



#print(z)
#print(f"{z:,}")
#print(z)

#https://docs.python.org/3/library/functions.html#round
#round(number, ndigits=None)

def main():
    #x = int(input("What's x? "))
    x = input("What's x? ")
    print("X squared is", square(x))

def square(n):

    return n * n

if __name__ == "__main__":
    main()








