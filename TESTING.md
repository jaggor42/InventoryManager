
# Inventory Manager Testing

This document records the tests performed on the Inventory Manager application.

## Test Results

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Missing file | Temporarily rename inventory.txt and run the program | Program starts with an empty inventory | Tested | Pass |
| 2 | Empty inventory | Select option 1 with no items | Displays "No inventory items found." | Tested | Pass |
| 3 | Add item | Add HDMI Cable, Electronics, 6 | Item is added and saved | Appeared in inventory with quantity 6 | Pass |
| 4 | Empty name | Enter a blank item name | Displays an error message | Tested | Pass |
| 5 | Duplicate name | Add laptop charger when Laptop Charger exists | Duplicate item is rejected | Tested | Pass |
| 6 | Invalid quantity | Enter "six" as the quantity | Displays a quantity error | Tested | Pass |
| 7 | Negative quantity | Enter -3 as the quantity | Rejects negative quantity | Tested | Pass |
| 8 | Update quantity | Update an existing item to 12 | Item quantity changes and is saved | Tested | Pass |
| 9 | Invalid item number | Enter 99 when updating an item | Displays an out-of-range error | Tested | Pass |
| 10 | Remove item | Remove an existing item | Item is removed and saved | Tested | Pass |
| 11 | Partial search | Search for CHARGER | Displays matching chargers regardless of capitalization | Tested | Pass |
| 12 | No-match search | Search for television | Displays "No inventory items matched your search." | Tested | Pass |
| 13 | Inventory summary | Select option 6 | Displays correct totals, low-stock count, and category counts | Tested | Pass |
| 14 | File persistence | Add or update an item, exit, and restart | Saved changes remain after restarting | Tested | Pass |

## Additional Tests

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 15 | Invalid menu option | Enter 9 | Displays an invalid choice message | Tested | Pass |
| 16 | Empty search | Enter only spaces | Displays an empty search error | Tested | Pass |
| 17 | Zero quantity | Add an item with quantity 0 | Item is accepted | Tested | Pass |
| 18 | Invalid category | Enter Office\|Supplies | Category is rejected | Tested | Pass |
| 19 | Category capitalization | Add items under Electronics and electronics | Both are counted as one category | Tested | Pass |
| 20 | Exit | Select option 7 | Displays goodbye message and exits normally | Tested | Pass |

## Testing Summary

Total tests: 20

Passed: 20

Failed: 0

Not yet tested: 0

## Notes

Tests are performed using Visual Studio Code and the Python terminal.

Any failed tests will be documented, corrected, and rerun before final submission.
