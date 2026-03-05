#https://cs50.harvard.edu/python/psets/2/twttr/

# Or another solution using filter function
# s = "".join(filter(lambda c: c != "o", s))
vowels = ["a", "e", "i", "o", "u"]
def main():


    word = input("Input: ")
    print("Output: " + convert(word))



def convert(word):
    new_word = ""
    for c in word:
        new_word = new_word + c

        for vowel in vowels:
            if (c.isupper()):
                if vowel.upper() == c.upper():
                    new_word = new_word.replace(f"{c.upper()}", "")
            else :
                if vowel == c:
                    new_word = new_word.replace(f"{c}", "")


    return(new_word)






main()
