inventory = {
    "Apples": 10,
    "Bananas": 15,
    "Oranges": 8,
    "Milk": 5,
    "Bread": 12
}

def display_inventory():
    print("\nCurrent Inventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")
    print()

while True:
    display_inventory()

    print("What would you like to do?")
    print("1. Buy item (add to inventory)")
    print("2. Sell item (remove from inventory)")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        item = input("Enter item name to buy: ").capitalize()
        if item in inventory:
            try:
                qty = int(input(f"Enter quantity of {item} to buy: "))
                if qty > 0:
                    inventory[item] += qty
                    print(f"{qty} {item}(s) added to inventory.")
                else:
                    print("Quantity must be positive.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not found in inventory.")

    elif choice == "2":
        item = input("Enter item name to sell: ").capitalize()
        if item in inventory:
            try:
                qty = int(input(f"Enter quantity of {item} to sell: "))
                if 0 < qty <= inventory[item]:
                    inventory[item] -= qty
                    print(f"{qty} {item}(s) sold.")
                else:
                    print("Invalid quantity. Not enough stock or non-positive value.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not found in inventory.")

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
