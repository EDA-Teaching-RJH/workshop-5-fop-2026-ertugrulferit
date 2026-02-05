VALID_COINS = {50, 20, 10, 5}
DENOMINATIONS = [50, 20, 10, 5]
DRINKS = {"1": ("Coffee", 75), "2": ("Hot Chocolate", 95),"3": ("Tea", 65), "4": ("Cappuccino", 100)}


def get_coin():
    while True:
        s = input("Insert coin (50, 20, 10, 5) in pence: ")
        try:
            coin = int(s)
        except ValueError:
            print("Invalid Input")
            continue
        if coin in VALID_COINS:
            return coin
        else:
            print("Unknown coin")


def update_total(current, coin):
    return current + coin


def calculate_change(amount):
    result = []
    remaining = amount
    for coin in DENOMINATIONS:
        while remaining >= coin:
            remaining -= coin
            result.append(coin)
    return result


def choose_drink():
    print("Select a drink:")
    for key, (name, price) in DRINKS.items():
        print(f"{key}) {name} - {price}p")
    while True:
        choice = input("Choice: ")
        if choice in DRINKS:
            return DRINKS[choice]
        print("Invalid choice")


def dispense_product_for_price(total_inserted, price):
    print("Purchase complete.")
    change = total_inserted - price
    if change <= 0:
        print("No change owed. Thank you.")
        return
    coins = calculate_change(change)
    if coins:
        coin_list = ', '.join(f"{c}p" for c in coins)
        print(f"Returning: {coin_list}")
    else:
        print(f"Change owed: {change}p")


def main():
    drink_name, price = choose_drink()
    total = 0
    print(f"Selected: {drink_name} — Price: {price}p")
    while total < price:
        coin = get_coin()
        total = update_total(total, coin)
        due = max(0, price - total)
        if due > 0:
            print(f"Amount due: {due}p")
    dispense_product_for_price(total, price)


if __name__ == "__main__":
    main()
