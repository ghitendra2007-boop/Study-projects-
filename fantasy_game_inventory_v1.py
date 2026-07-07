#this is a program that will show the inventory items in a fnatansy game and ti works even list is being updated or more items are bing added to the lsit 

#inventory:
stuff = {'rope': 1 ,'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#display
def display(inventory):
    global item_total
    print('inventory')
    item_total = 0
    for k,v in stuff.items():
        print(str(k) + ' = '+str(v))
        item_total = item_total + int(v)





#calling fucntion
display(stuff)
print('Total Items:')
print(int(item_total))
