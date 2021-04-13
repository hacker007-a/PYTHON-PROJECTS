def addition(a,b):
    add = a+b
    print(add)

def subtraction(a,b):
    sub = a-b
    print(sub)

def multiplication(a,b):
    multiply = a*b
    print(multiply)

def division(a,b):
    divide = a/b
    print(divide)


while True:
    
    x = int(input('Enter number: '))
    y = int(input('Enter sec number: '))
    lst = ['addition', 'subtraction', 'multiplication', 'division']
    print('What u wnt to do?: ', lst)
    n = input('Your choice: ')
    if n == lst[0]:
        addition(x,y)
        
    elif n == lst[1]:
        subtraction(x,y)
        
    elif n == lst[2]:
        multiplication(x,y)
        
    elif n == lst[3]:
        division(x,y)
        

    else:
        print('wrong input')

    m = input('press q to exit or ENTER to continue: ')
    # print('Press q to exit')
    if m =='q':
        break
