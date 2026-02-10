def main():

    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    total = float(interpreter(x,y,z))
    print(total)


def interpreter(x,y,z):
    match y:
        case "+":
            total = x + z
            return total
        case "-":
            total = x - z
            return total
        case "*":
            total = x * z
            return total
        case "/":
            total =x / z
            return total

main()




