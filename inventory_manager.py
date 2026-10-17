"""Inventory Manager: A command-line inventory tracking application.

Author: Johnny Aggor
Course: CPS 310
Project: Inventory Manager
"""

INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Display the available Inventory Manager menu options."""
    print("\nInventory Manager")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")


def load_inventory(filename):
    """Load inventory items from a text file into a list of dictionaries."""
    inventory = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    name, category, quantity = line.split("|")

                    item = {
                        "name": name,
                        "category": category,
                        "quantity": int(quantity)
                    }

                    inventory.append(item)

    except FileNotFoundError:
        return []

    return inventory


def save_inventory(inventory, filename):
    """Save all inventory items to a text file."""
    with open(filename, "w") as file:
        for item in inventory:
            name = item["name"]
            category = item["category"]
            quantity = item["quantity"]

            file.write(f"{name}|{category}|{quantity}\n")


def main():
    """Run the Inventory Manager menu until the user exits."""
    inventory = load_inventory(INVENTORY_FILE)
    
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            print("This feature has not been implemented yet.")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

    
