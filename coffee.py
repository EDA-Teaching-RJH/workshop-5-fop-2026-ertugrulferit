##Statement of Requirements:
# Write a program that simulates a coffee vending machine. 
# The machine should accept coins (50p, 20p, 10p, 5p) and keep track of thetotal amount inserted. 
# The price of a cup of coffee is 75p. 
# The program should continue to prompt the user to insert coins until the total amount inserted is equal to or greater than the price of the coffee. 
# Once the required amount is reached, the program should calculate and display any change that needs to be returned to the user.
# If a non integer coin is inserted, the program should display an error message and prompt the user to insert a valid coin.
# The program must not crash if the user enters non-integer data. It should catch the error (using `try/except`), inform the user "Invalid Input," and ask for the coin again.
price = 75
def main():
    total_coins = 0
    while total_coins < price:
        coin_input = input("Insert coin (50p, 20p, 10p, 5p): ")
        if coin_input == "50":
            total_coins += 50
        elif coin_input == "20":
            total_coins += 20
        elif coin_input == "10":
            total_coins += 10
        elif coin_input == "5":
            total_coins += 5
        else:
            try:
                coin_value = int(coin_input)
                if coin_value in [50, 20, 10, 5]:
                    total_coins += coin_value
                else:
                    print("Invalid coin. Please insert a valid coin.")
            except ValueError:
                print("Invalid Input. Please insert a valid coin.")
    if total_coins >= price:
        change = total_coins - price
        print(f"Total inserted: {total_coins}p. change: {change}p.")
    else:        print(f"Total inserted: {total_coins}p. Not enough coins inserted.")
if __name__ == "__main__":    
    main()
    

      
