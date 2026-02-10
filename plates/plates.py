"""

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate;
AAA22A would not be acceptable.
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

"""



def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")


    else:
        print("Invalid")





def is_valid(s):

    if is_plate_length_correct(s) == False:
        return False

    elif is_alnum(s) == True:

            if has_numbers(s) == True:

                if is_2_first_alpha(s) == True:

                    if is_first_number_start_by_0(s) == False:
                        if is_number_in_the_middle(s) == False:
                            return True
                        else:
                            return False
                    else:
                        return False

                else:
                    return False
            else:
                return True


def is_2_first_alpha(s):

    two_first_characters = ""
    if 2 <= len(s) <= 6:
        for c in s:
            two_first_characters = two_first_characters + c
            if len(two_first_characters) == 2:
                if two_first_characters.isalpha() == True:

                    return True
                else:
                    return False

def is_last_character_numeric(s):
    last_character = s[-1]
    if last_character.isnumeric():
        return True
    else:
        return False

def has_numbers(s):
        numbers = ""
        for c in s:
            if (c.isnumeric() == True):
                numbers = numbers + c

        if (len(numbers) > 0):
            return True
        else:
            return False

def is_plate_length_correct(s):
    if 6 >= len(s) >= 2:
        return True
    else :
        return False

def is_alnum(s):
    if s.isalnum() == True:
        return  True
    else:
        return False

def is_first_number_start_by_0(s):
    index = s.find('0')            #find 0
    if index != -1:                #If we found 0
        if (s[index-1].isalpha()): #Does character before 0 is a letter ?
            return True            #if it is true it means that there is a letter before 0, it starts by 0
        else:
            return False           #if there is no letter it means it is a number , so that it does not start by 0
    return False                   #0 is never found here

def is_number_in_the_middle(s):
    numbers = ""
    for c in s :
        if c.isnumeric() == True:
            numbers = numbers + c

    if s.endswith(numbers) == True:
        #print("number")
        return False
    else :
        return True




















main()
