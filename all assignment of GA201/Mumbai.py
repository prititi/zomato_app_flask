# Snack Inventory Management System

# Function to add a snack to the inventory
def add_snack(snack_id, snack_name, price):
    snack = {
        'id': snack_id,
        'name': snack_name,
        'price': price,
        'available': True
    }
    inventory.append(snack)

# Function to remove a snack from the inventory
def remove_snack(snack_id):
    for snack in inventory:
        if snack['id'] == snack_id:
            inventory.remove(snack)
            return True
    return False

# Function to update the availability of a snack
def update_availability(snack_id, available):
    for snack in inventory:
        if snack['id'] == snack_id:
            snack['available'] = available
            return True
    return False

# Function to record a snack sale
def record_sale(snack_id):
    for snack in inventory:
        if snack['id'] == snack_id and snack['available']:
            snack['available'] = False
            return True
    return False

# Function to display the inventory
def display_inventory():
    print("Snack Inventory:")
    if len(inventory) == 0:
        print("No snacks available.")
    else:
        for snack in inventory:
            print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Available: {snack['available']}")

# Function to display the sales records
def display_sales_records():
    print("Sales Records:")
    if len(inventory) == 0:
        print("No snacks sold.")
    else:
        sold_snacks = [snack for snack in inventory if not snack['available']]
        if len(sold_snacks) == 0:
            print("No snacks sold.")
        else:
            for snack in sold_snacks:
                print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}")

# Main program
inventory = []

while True:
    print("\n====== Mumbai Munchies Canteen Management ======")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update the availability of a snack")
    print("4. Record a snack sale")
    print("5. Display the inventory")
    print("6. Display the sales records")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        snack_id = input("Enter the snack ID: ")
        snack_name = input("Enter the snack name: ")
        price = float(input("Enter the snack price: "))
        add_snack(snack_id, snack_name, price)
        print("Snack added to the inventory.")
    elif choice == '2':
        snack_id = input("Enter the snack ID: ")
        if remove_snack(snack_id):
            print("Snack removed from the inventory.")
        else:
            print("Snack not found in the inventory.")
    elif choice == '3':
        snack_id = input("Enter the snack ID: ")
        available = input("Is the snack available (yes/no)? ").lower()
        if available == 'yes':
            update_availability(snack_id, True)
        elif available == 'no':
            update_availability(snack_id, False)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    elif choice == '4':
        snack_id = input("Enter the snack ID: ")
        if record_sale(snack_id):
            print("Snack sale recorded.")
        else:
            print("Snack not available or not found in the inventory.")
    elif choice == '5':
        display_inventory()
    elif choice == '6':
        display_sales_records()
    elif choice == '0':
        print("Thank you for using Mumbai Munchies Canteen Management. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
