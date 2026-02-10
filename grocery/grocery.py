def main():
    dic = {}
    number_item = 1

    while True:
        try:
            item = input("").upper()

            if  item in dic:
                number_item = dic[item] + 1
                dic[item] = number_item


            else:

                 number_item = 1
                 dic[item] = number_item


        except KeyError:
            print("key errors!!!!!")
            
        except EOFError:
            for fruit in sorted(dic):
                print(f"{dic[fruit]}" + " " + f"{fruit}")

            break




main()
