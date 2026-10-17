# Inventory Manager

## Project Description

Inventory Manager is a command-line Python application developed for CPS 310 at Central Michigan University. The program allows users to manage inventory items by adding, viewing, updating, removing, and searching for items. Inventory information is saved in a text file so that changes remain available after the program closes.

## Current Features

- View all inventory items in a numbered list.
- Add new items with a name, category, and quantity.
- Update the quantity of existing items.
- Remove items from the inventory.
- Search for items using partial or complete names without case sensitivity.
- Display inventory summaries, including total quantities, low-stock items, and category counts.
- Validate user input to prevent invalid entries.
- Save and load inventory data using a text file.

## Requirements

- Python 3
- Visual Studio Code or another code editor
- A terminal or command-line interface
- Git (for version control)

The program uses only built-in Python functionality and does not require additional libraries.

## Project Files

| File | Description |
|---|---|
| `inventory_manager.py` | Contains the main Python program and inventory functions. |
| `inventory.txt` | Stores inventory items in a text file. |
| `README.md` | Provides project information and instructions. |
| `TESTING.md` | Documents testing procedures and results. |
| `AI_USAGE.md` | Documents how artificial intelligence assisted development. |
| `.gitignore` | Prevents unnecessary or sensitive files from being tracked by Git. |

## Inventory Data Format

Inventory items are stored in `inventory.txt` using the following format:

`Name|Category|Quantity`

Example:

```text
Laptop Charger|Electronics|8
Printer Paper|Office Supplies|25
Dry-Erase Markers|Classroom Supplies|4
```

Each item contains a name, category, and nonnegative whole-number quantity.

## Running the Program

1. Open the `InventoryManager` folder in Visual Studio Code.
2. Open the integrated terminal.
3. Make sure the terminal is in the project directory.
4. Run the following command:

```powershell
python inventory_manager.py
```

The program will display the main menu.

## Menu Options

```text
Inventory Manager

1. View inventory
2. Add an item
3. Update an item quantity
4. Remove an item
5. Search inventory
6. View inventory summary
7. Exit
```

Users can enter a number from 1 through 7 to select an option. Invalid selections display an error message.

## Sample Interaction

The following example demonstrates adding an inventory item:

```text
Enter your choice (1-7): 2
Enter the item name: HDMI Cable
Enter the category: Electronics
Enter the quantity: 6
Item added successfully.
```

The program adds the item to the inventory list and saves the updated information to `inventory.txt`.

## Testing Summary

Testing covers inventory loading, viewing, adding, updating, removing, searching, input validation, summary calculations, and file persistence.

Detailed test cases, expected results, and actual results are documented in `TESTING.md`.

## Git and GitHub Development

Git was used to track changes throughout development. Features were implemented through incremental commits with descriptive commit messages.

The inventory search feature was developed using a separate branch named `feature/inventory-search`.

A GitHub issue was created to describe the search requirements. The feature was then developed on its own branch and reviewed through a pull request before merging into `main`.

## Known Limitations

- The application uses a command-line interface rather than a graphical interface.

Inventory records are stored in a local text file rather than a database.

The application is designed for one user at a time.

Inventory items do not include prices or supplier information.

The program assumes existing inventory records follow the required file format.

Possible Future Improvements

Add a graphical user interface.

Allow users to sort inventory by name, category, or quantity.

Add low-stock notifications.

Track inventory prices and total inventory value.

Store inventory information in a database.

Add support for exporting inventory reports.

Author

Johnny Aggor

CPS 310 — Central Michigan University