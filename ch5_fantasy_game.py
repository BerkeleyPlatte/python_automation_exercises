stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


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
        
        
displayInventory(stuff)



def addToInventory(inventory, addedItems):
    for each in addedItems:
        for key, value in inventory.items():
            if each == key:
                inventory[key] = value + 1
        inventory.setdefault(each, 1)
    displayInventory(inventory)
    
    
addToInventory(stuff, dragonLoot) 
    