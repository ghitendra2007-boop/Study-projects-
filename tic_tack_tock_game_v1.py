#this is a detailed version of a tick tack toe game build by me without using external help or structure

#representation
def gui():
    print( str(input1) + ' | ' + str(input2)  +' | ' + str(input3))
    print( '-'*18)
    print( str(input4) + ' | ' + str(input5) + ' | ' + str(input6))
    print( '-'*18)
    print( str(input7) + ' | ' + str(input8) + ' | ' + str(input9))


#variables

name1 = ''
name2 = ''
finalresult = False
input1 = '1'
input2 = '2'
input3 = '3'
input4 = '4'
input5 = '5'
input6 = '6'
input7 = '7'
input8 = '8'
input9 = '9'
mistake = None









#choosing system
def choosingsystem():
    global input1,input2,input3,input4,input5,input6,input7,input8,input9,mistake
    print('PLease choose where you wana play your move (please choose one that is being not played already)')
    move = input()
    if move == '1':
        while input1 == '1':
            if i % 2 == 0:
                input1 = 'O'
            else :
                input1 = 'X'
            mistake = False
            
            return input1
    
    elif move == '2':
        while input2 == '2':
            if i % 2 == 0:
                input2 = 'O'
            else :
                input2 = 'X'
            mistake = False

            return input2
    
    elif move == '3':
        while input3 == '3':
            if i % 2 == 0:
                input3 = 'O'
            else :
                input3 = 'X'
            mistake = False

            return input3
    
    elif move == '4':
        while input4 == '4':
            if i % 2 == 0:
                input4 = 'O'
            else :
                input4 ='X'
            mistake = False

            return input4
    
    elif move == '5':
        while input5 == '5':
            if i % 2 == 0:
                input5 = 'O'
            else:
                input5 = 'X'
            mistake = False

            return input5
    
    elif move == '6':
        while input6 == '6':
            if i % 2 == 0:
                input6 = 'O'
            else :
                input6 ='X'
            mistake = False

            return input6
    
    elif move == '7':
        while input7 == '7':
            if i % 2 == 0:
                input7 = 'O'
            else :
                input7 = 'X'
            mistake = False

            return input7
    
    elif move == '8':
        while input8 == '8':
            if i % 2 == 0:
                input8 ='O'
            else :
                input8 = 'X'
            mistake = False

            return input8
    
    elif move == '9':
        while input9 == '9':
            if i % 2 == 0:
                input9 = 'O'
            else :
                input9 = 'X'
            mistake = False

            return input9
    
    else :
        print('i think i said to choose a empty place')
    
    return mistake
    


#result anounser
def anouncer(result):
    if result == 'O':
        print(name1 + ' wins!!')
    elif result == 'X':
        print(name2 + ' wins!!')
    



#result analiser
def result():
    global finalresult
    if input1 == input5 == input9:
        anouncer(input1)
        finalresult = True
    
    elif input1 == input2 == input3:
        anouncer(input1)
        finalresult = True
    
    elif input1 == input4 == input7:
        anouncer(input1)
        finalresult = True
    
    elif input2 == input5 == input8:
        anouncer(input2)
        finalresult = True
    
    elif input3 == input6 == input9:
        anouncer(input3)
        finalresult = True
    
    elif input4 == input5 == input6:
        anouncer(input4)
        finalresult = True

    elif input7 == input8 == input9:
        anouncer(input7)
        finalresult = True

    elif input3 == input5 == input7:
        anouncer(input3)
        finalresult = True

    return finalresult



    









#input system
def inputsytem():
            global i,mistake
            for i in range(0,9):
                gui()
                
                if finalresult == True:
                    break
                
                elif i % 2 == 0:
                    mistake = True
                    while mistake == True:
                        print(str(name1) + ' tern')
                        choosingsystem()
                        result()

                else :
                    mistake = True
                    while mistake == True:
                        print(str(name2) + ' tern')
                        choosingsystem()
                        result()









#final result body 
print('Hello this is simple tic tack tock game')
print('please enter player names')
print('player 1 name:')
name1 = input()
print('player 2 name:')
name2 = input()

print( name1 + ' vs '+ name2)
inputsytem()
print('Thank you for playing')



