#project chapter 4-1 (comma code)


#lists
spam = ['apple','bet','hello','milk','hi','by']
newspam = spam[:(len(spam))-1]


#variables
number = None
variable = None

#list mkaing 
def listmaking():
    finalspam = ''
    for  variable in range(0,len(newspam)):
        finalspam = finalspam + newspam[variable]
    return finalspam






#main program
for number in range(0,int(len(newspam))):
    if number % 2 == 0:
        newspam.insert(1 + number,',')
    else:
        continue

print( str(listmaking()) + ' and ' + str(spam[-1]))