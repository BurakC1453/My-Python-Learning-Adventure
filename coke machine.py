def main ():
    user_preference = input ("Hello good day dear customer, do you want to get some coke ? (1: Yes, 0: No)")
    if user_preference != "1":
        print("Your choice dear customer , have a nice day...")
        return
    coke_amount = 0
    amount_of_coins_inserted = 0
    while True:
        amount_of_coins_inserted += int(input("Insert your coins : "))
        if amount_of_coins_inserted < 50:
            print(f"Please insert {50 - amount_of_coins_inserted} more cents.")
        else:
            while amount_of_coins_inserted >= 50:
                coke_amount += 1
                print("Here is your coke, enjoy!")
                amount_of_coins_inserted -= 50
            print("Do you want to get more coke? (1: Yes, 0: No)")
            if input() != "1":
                break
    if amount_of_coins_inserted > 0:
        print(f"Hey, dont forget the extra {amount_of_coins_inserted} cents you inserted, here is your change.")
    print("Thanks for your purchase...")        
main()
