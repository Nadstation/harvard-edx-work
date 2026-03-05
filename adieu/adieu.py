import inflect

def main():
    names = []

    while(True):
        try:
            entry = input("Name: ")
            names.append(entry)

        except EOFError:
            pre = inflect.engine()
            fix = pre.join(names)

            final = f"Adieu, adieu, to {fix}"



            print("\n" + final)
            break

















main()


