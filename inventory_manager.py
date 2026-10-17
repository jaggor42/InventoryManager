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


def view_inventory(inventory):
    """Display all inventory items in a numbered list."""
    if not inventory:
        print("No inventory items found.")
        return

    print("\nInventory:")

    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")



def add_item(inventory):
    """Add a new inventory item after validating user input."""
    name = input("Enter the item name: ").strip()

    if not name or "|" in name:
        print("Invalid item name.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("An item with this name already exists.")
            return

    category = input("Enter the category: ").strip()

    if not category or "|" in category:
        print("Invalid category.")
        return

    quantity_input = input("Enter the quantity: ").strip()

    if not quantity_input.isdecimal():
        print("Quantity must be a nonnegative whole number.")
        return

    quantity = int(quantity_input)

    item = {
        "name": name,
        "category": category,
        "quantity": quantity
    }

    inventory.append(item)
    save_inventory(inventory, INVENTORY_FILE)

    print("Item added successfully.")



def update_quantity(inventory):
    """Update the quantity of an existing inventory item."""
    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    item_input = input("Enter the item number to update: ").strip()

    if not item_input.isdecimal():
        print("Invalid item number.")
        return

    item_number = int(item_input)

    if item_number < 1 or item_number > len(inventory):
        print("Item number is out of range.")
        return

    quantity_input = input("Enter the new quantity: ").strip()

    if not quantity_input.isdecimal():
        print("Quantity must be a nonnegative whole number.")
        return

    new_quantity = int(quantity_input)

    item = inventory[item_number - 1]
    item["quantity"] = new_quantity

    save_inventory(inventory, INVENTORY_FILE)

    print(f"{item['name']} quantity updated to {new_quantity}.")



def remove_item(inventory):
    """Remove an inventory item using its displayed number."""
    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    item_input = input("Enter the item number to remove: ").strip()

    if not item_input.isdecimal():
        print("Invalid item number.")
        return

    item_number = int(item_input)

    if item_number < 1 or item_number > len(inventory):
        print("Item number is out of range.")
        return

    removed_item = inventory.pop(item_number - 1)

    save_inventory(inventory, INVENTORY_FILE)

    print(f"Item removed: {removed_item['name']}")



def search_inventory(inventory):
    """Search inventory items by name, ignoring capitalization."""
    search_term = input("Enter an item name to search: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    matches = []

    for item in inventory:
        if search_term.lower() in item["name"].lower():
            matches.append(item)

    if not matches:
        print("No inventory items matched your search.")
        return

    print("\nSearch Results:")

    for number, item in enumerate(matches, start=1):
        print(f"{number}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")



def display_summary(inventory):
    """Display inventory totals, low-stock items, and category counts."""
    unique_items = len(inventory)
    total_quantity = 0
    low_stock = 0
    categories = {}

    for item in inventory:
        total_quantity += item["quantity"]

        if item["quantity"] < 5:
            low_stock += 1

        category = item["category"].lower()

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    print("\nInventory Summary")
    print(f"Unique items: {unique_items}")
    print(f"Total quantity: {total_quantity}")
    print(f"Low-stock items: {low_stock}")

    print("\nItems by category:")

    for category, count in categories.items():
        print(f"{category.title()}: {count}")

def main():
    """Run the Inventory Manager menu until the user exits."""
    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            search_inventory(inventory)
        elif choice == "6":
            display_summary(inventory)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
