def displayInventory(inventory):
    total = []
    for value in inventory.values():
        total.append(value)
    to_print = []
    for key, value in inventory.items():
        to_print.append(f'{value} {key} \n')
    to_print.append(f'Total number of items: {sum(total)}')
    to_print[:0] = ['Inventory:\n']
    for each in to_print:
        print(each)
        
        
displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})


def addToInventory(inventory, addedItems):
    addedItems_dict = {}
    for each in addedItems:
        addedItems_dict[each] = 1
    