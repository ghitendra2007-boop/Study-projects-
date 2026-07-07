#this code add dragon loot in fomr of list to our inventory in form of dictionary

#list adder
def addinventory(player,loot):


    for i in range(0,int(len(loot))):
        item = loot[i]
        if item in player:
            player[item] = player[item] + 1
        else:
            player[item] = 1
    return player
    

    



#player inventory
inv = {'gold coin': 42, 'rope': 1}
dragonloot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addinventory(inv,dragonloot)
print(inv)