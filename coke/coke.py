def main():
    amount_due = 50

    print(f"Amount Due: {amount_due}")
    while amount_due != 0:



        inserted_coin = int(input("Insert Coin: "))

        match inserted_coin:
            case 25 | 10 | 5 :
                amount_due = amount_due - inserted_coin
                if amount_due == 0:
                    print(f"Change Owed: {amount_due}")
                    break

                elif amount_due < 0:
                    print(f"Change Owed: {abs(amount_due)}")
                    break
                else:
                    print(f"Amount Due: {amount_due}")
            case _:
                print(f"Amount Due: {amount_due}")






def convert():
    print("do nothing for now")





main()
