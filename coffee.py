#Statement of Requirements

#Functional Requirements:
# Accept integer coin inputs in pence: 50, 20, 10, 5.
# When total inserted >= 75p, complete the purchase and return change (total - 75p).
#Non-Functional Requirements:
# If the user enters non-integer data, do not crash. Print "Invalid Input" and prompt again.
# Ignore unknown integer denominations (print "Unknown coin" and prompt again).

VALID_COINS = {50, 20, 10, 5}
PRICE = 75
def get_coin():
    while True:
        entercoin = input("Insert coin (50, 20, 10, 5) in pence: ")
        try:
            coin = int(entercoin)
        except ValueError:
            print("Invalid Input")
            continue
        if coin in VALID_COINS:
            return coin
        else:
            print("Unknown coin")

def update_total(current, coin):
    return current + coin

def dispense_product(total_inserted):
    change = total_inserted - PRICE
    print("Purchase complete.")
    if change > 0:
        print(f"Change: {change}p")
    else:
        print("No change:(")

def main():
    total = 0
    print(f"Price: {PRICE}p")
    while total < PRICE:
        coin = get_coin()
        total = update_total(total, coin)
        due = max(0, PRICE - total)
        if due > 0:
            print(f"Amount due: {due}p")
    dispense_product(total)

if __name__ == "__main__":
    main()

      


