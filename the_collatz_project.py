#practice project chapter 3 

#collatz function

def collatz(number):
    if number % 2 == 0:
        solution = int(number // 2)

    elif number % 2 == 1:
        solution = int(3*number + 1)
    
    else:
        print('please enter a intiger')

    
    return solution 


    


#variables
number = None
finalsolution = None
#user part

print('Please enter a number and avoid entering a non integral value')
number = int(input())
while finalsolution != 1:
    finalsolution = collatz(number)
    number = finalsolution
    print(finalsolution)
    
    
    

