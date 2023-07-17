menu = {
    1: {"name": "Margherita Pizza", "price": 12.99, "available": True},
    2: {"name": "Pasta Alfredo", "price": 9.99, "available": True},
    3: {"name": "Garlic Breadsticks", "price": 4.99, "available": True},
    # Add more dishes as needed
}
menu = {
    1: {"name": "Margherita Pizza", "price": 12.99, "available": True},
    2: {"name": "Pasta Alfredo", "price": 9.99, "available": True},
    3: {"name": "Garlic Breadsticks", "price": 4.99, "available": True},
    # Add more dishes as needed
}
def display_menu():
    print("Menu:")
    for dish_id, dish_info in menu.items():
        availability = "Available" if dish_info["available"] else "Not Available"
        print(f"{dish_id}. {dish_info['name']} - ${dish_info['price']} ({availability})")

def add_dish():
    dish_id = len(menu) + 1
    name = input("Enter the name of the new dish: ")
    price = float(input("Enter the price of the new dish: "))
    availability = input("Is the dish available? (yes/no): ").lower() == "yes"

    menu[dish_id] = {"name": name, "price": price, "available": availability}
    print(f"{name} has been added to the menu.")

def remove_dish():
    dish_id = int(input("Enter the dish ID to remove: "))

    if dish_id in menu:
        del menu[dish_id]
        print("Dish removed from the menu.")
    else:
        print("Dish not found in the menu.")

def update_dish_availability():
    dish_id = int(input("Enter the dish ID to update availability: "))
    
    if dish_id in menu:
        availability = input("Is the dish available? (yes/no): ").lower() == "yes"
        menu[dish_id]["available"] = availability
        print("Availability updated.")
    else:
        print("Dish not found in the menu.")



orders = []
order_id_counter = 1
def take_order():
    global order_id_counter
    customer_name = input("Enter customer's name: ")
    dish_ids = input("Enter dish IDs (comma-separated) the customer wants to order: ")
    dish_ids = [int(dish_id.strip()) for dish_id in dish_ids.split(",")]

    for dish_id in dish_ids:
        if dish_id not in menu or not menu[dish_id]["available"]:
            print(f"Dish ID {dish_id} is invalid or not available. Order canceled.")
            return

    order = {
        "order_id": order_id_counter,
        "customer_name": customer_name,
        "dish_ids": dish_ids,
        "status": "received"
    }

    orders.append(order)
    order_id_counter += 1
    print("Order received and added to the system.")

def update_order_status():
    order_id = int(input("Enter the order ID to update: "))
    status = input("Enter the new status of the order: ")

    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = status
            print("Order status updated.")
            return

    print("Order ID not found.")

def review_orders():
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print(f"Customer Name: {order['customer_name']}")
        print("Dishes:")
        for dish_id in order["dish_ids"]:
            print(f"- {menu[dish_id]['name']} (${menu[dish_id]['price']})")
        print(f"Status: {order['status']}")
        print()

import json

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data["menu"], data["orders"]
    except FileNotFoundError:
        return {}, []

menu, orders = load_data()


def user_interface():


    while True:
        print("Zesty Zomato - Food Delivery System")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            remove_dish()
        elif choice == "4":
            update_dish_availability()
        elif choice == "5":
            take_order()
        elif choice == "6":
            update_order_status()
        elif choice == "7":
            review_orders()
        elif choice == "8":
            print("Thank you for using Zesty Zomato. Have a great day!")
            save_data(menu, orders)
            break
        else:
            print("Invalid choice. Please try again.")

def save_data(menu, orders):
    data = {
        "menu": menu,
        "orders": orders
    }

    with open("data.json", "w") as file:
        json.dump(data, file)

user_interface()
