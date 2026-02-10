def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x_y = fraction.split("/")
            x = int(x_y[0])
            y = int(x_y[1])

            #If, though, X or Y is not an integer, X is greater than Y,
            # or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
            # Be sure to catch any exceptions like ValueError or ZeroDivisionError.

            if x < 0 or x > y:
                raise ValueError


            elif (x/y == 1):
                print("F")
                break
            elif round((x/y)*100) <= 1:
                print("E")
                break
            elif round((x/y)*100) >= 99:
                print("F")
                break
            else:
                print(f"{round((x/y)*100)}%")
                break

        except ValueError:
            print("Value error!!!!!!!!")
            pass
        except ZeroDivisionError:
            print("ZeroDivisionError!!!!!!!!")
            pass


main()




