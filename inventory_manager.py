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


def main():
    """Run the Inventory Manager menu until the user exits."""
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
