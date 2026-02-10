def main():
    camelCase = input("camelCase: ")
    print(convert(camelCase))


def convert(camelCase):
    new_string = ""
    is_first_letter_upper = camelCase[0].isupper()

    if is_first_letter_upper == True:
        camelCase = camelCase[0].lower() + camelCase[1:]

    for c in camelCase:


        isUpper = c.isupper()


        if (isUpper) == False:
            new_string = new_string + c

        elif(isUpper) == True:
            new_string = new_string + "_"
            c = c.lower()
            new_string = new_string + c

    return("snake_case: " + new_string)




main()
