"""
We want to make a vending machine program that will:

* Open a file which contains stock in the format:
  <beverage> <cost> <quantity>

* If the format is incorrect (qty is missing for example)
  Our program should show an error message stating
  What is wrong with it.

* Allow the user to select an option from 0 - n-1 in
  the vending machine menu

* Handle checking out the item and for the user to pay
  for it. This should ask for the user to insert
  * $1, $2, $5, $10 or $20 until the amount of change is
  greater than or equal to the cost of the beverage

* The program should not allow the user to pay unless the stock
  is greater than 0.
"""
import sys

quit = False

def load_stock(filepath):
    items = {}
    with open(filepath, 'r') as stock:
        for line in stock:
            spl = line.split()
            items[spl[0]] = [spl[1], spl[2]]
    return items

def display_items(items):
    for i, k in enumerate(items):
        print('[' + str(i) + ']' + ' ' + str(k))

def user_select(items):
    global quit
    print('Select an option between 0 and ' + str(len(items)-1) + ' or press \'q\' to quit')
    i = input()
    item = None
    if i != 'q':
        i = int(i)
        for j, k in enumerate(items):
            if i == j:
                item = (k, items[k][0], items[k][1])
    else:
        quit = True
    return item

def checkout(item):
    print('Insert $1, $2, $5, $10 or $20 or press \'c\' to cancel')
    cost = float(item[1])
    cancelled = False
    while cost > 0 and not cancelled:
        change = input()
        if change != 'c':
            change = int(change)
            if check_change_is_valid(change):
                cost -= change
        else:
            cancelled = True
    if not cancelled:
        print("Item has been paid for, Thank you!")
    else:
        print('Your order has been cancelled')

def check_change_is_valid(change):
    valid_change = [1, 2, 5, 10, 20]
    is_valid = False
    for c in valid_change:
        if change == c:
            is_valid = True
    return is_valid


items = load_stock(sys.argv[1])
while not quit:
    display_items(items)
    item = user_select(items)
    if not quit and (item is not None):
        checkout(item)
