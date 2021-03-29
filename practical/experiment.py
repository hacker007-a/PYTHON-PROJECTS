# # ================+============================================================================#
# # half christmas tree :)
# '''for i in range(1, 9):
#     for j in range(1, i - 1):
#         print("A", end=' ')
#     print()
# for i in range(1, 9):
#     for j in range(i + 1):
#         print("A", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(i + 2):
#         print("A", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(i + 3):
#         print("A", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(i + 4):
#         print("A", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(i - 1, i + 4):
#         print("=", end=' ')
#     print()
# #------------------------------------------------------------------------#
#
# # nested 'for' loop
# for i in range(1, 9):
#     for j in range(1, i + 1):
#         print("#", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(i - 1, 8):
#         print("#", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(1, i + 1):
#         print("#", end=' ')
#     print()
#
# for i in range(1, 9):
#     for j in range(i - 1, 8):
#         print("#", end=' ')
#     print()
# for i in range(1, 9):
#     for j in range(1, i + 1):
#         print("#", end=" ")
#     print()
# for i in range(1, 9):
#     for j in range(i - 1, 8):
#         print("#", end=' ')
#     print()
#
# for i in range(1, 25):
#     for j in range(25-i):
#         print("V", end=' ')
#     print() '''
# #----------------------------------------------------------------------------------------------------------#
# # upper half
#
# n = 13
# k = round(n/2)*2
# for i in range(0, n, 2):
#     for j in range(0, k+1):
#         print(end=' ')
#     for j in range(0, i+1):
#         print("*", end=' ')
#     k-=2
#     print()
# # lower half
# k = 1
# for i in range(n-1, 0 ,-2):
#     for j in range(0, k+2):
#         print(end = ' ')
#     for j in range(0, i-1):
#         print("*", end = ' ')
#     k+=2
#     print()
#
# n=9
# j=n-1
# print(" "*(n)+'*')
# for i in range(1,2*n):
#     if i > n:
#         print(' '*(i-n)+'*'+' '*(2*j-1)+"*")
#         j-=1
#     else:
#         print(' '*(n-i)+'*'+' '*(2*i-1)+"*")
# if n > 1:
#     print(" "*n+"*")
try:
    print('How many rows u want to print? ')
    n = int(input())
    n1 = int(input('Type 1 or 0 '))
    bol = bool(n1)
    if n1 == True:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print("*", end=' ')
            print()

    elif n1 == False:
        for i in range(1, n+1):
            for j in range(i - 1, n):
                print("*", end=' ')
            print()
except Exception as e:
    print('Invalid input!!!')

###########################################################################################################
###########################################################################################################

#
# # Currency Converter
# with open('currencyData.txt') as f:
#     lines = f.readlines()
# #
# # print(lines)
# currencyDict = {}
# for line in lines:
#     parsed = line.split('\t')
#     currencyDict[parsed[0]] = parsed[1]
#
# # print(currencyDict)
# amount = float(input('Enter amount: '))
# print('Enter the name of currency you want to'
#       'convert this amount to? \n Available options: ')
# [print(item) for item in currencyDict.keys()]
# currency = input('Please enter one of the values: ')
# print(f'{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}')



# for i in range(1,10):
#     for j in range(2,11):
#         print('#', end = ' ')
#     print()


# for i in range(0,5):
#     print('*'*i) # important