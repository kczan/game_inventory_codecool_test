
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    for key in inventory:
        print(str(key) + ': ' + str(inventory[key]))
    pass


def add_to_inventory(inventory, added_items):
    for loot_item in added_items:
        if loot_item in inventory.keys():
            inventory[loot_item] = inventory[loot_item] + 1
        else:
            inventory[loot_item] = 1
    display_inventory(inventory)
    pass


def print_table(inventory, order=None):
    if order == 'count,asc':
        inventory = {k: v for k, v in sorted(inventory.items(), key=lambda item: item[1])}
    elif order == 'count,desc':
        inventory = {k: v for k, v in sorted(inventory.items(), key=lambda item: item[1], reverse=True)}
    print('-'*17)
    print('item name'.rjust(9), '|', 'count'.rjust(5))
    print('-' * 17)
    for k, v in inventory.items():
        print(f'{str(k).rjust(9)}', '|', f'{str(v).rjust(5)}')
    print('-' * 17)
    pass


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, 'r') as imported_inventory:
        imported_items = imported_inventory.read().split(',')
        add_to_inventory(inventory, imported_items)
    pass


def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, 'w') as exported_inventory:
        exported_items = ''
        for item in inventory.keys():
            print(inventory[item])
            for index in range(0, inventory[item]):
                exported_items = exported_items + item + ','
        exported_items = exported_items[:-1]
        exported_inventory.write(exported_items)
    pass


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
#display_inventory(inv)
add_to_inventory(inv, dragon_loot)
import_inventory(inv,'test_inventory.csv')
#print_table(inv,'count,asc')
export_inventory(inv)
print_table(inv, order='count,desc')