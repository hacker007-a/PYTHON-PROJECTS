import random
# fnum=random.random()*(95-45)+45
# inum=math.ceil(fnum)
# print("Random numbers between 95,45: ")
# print(fnum)
# print("nearest higher integer: ", inum
# # =================================================================#
#
# to find the area of the triangle using herons formula
# import math
# a = int(input("Enter first side of the triangle: "))
# b = int(input("Enter second side of the triangle: "))
# c = int(input("Enter third side of the triangle: "))
# s = a + b + c / 2
# ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
# print("Sides of the trangle: ", a,'units', b,'units', c,'units')
# print("Area of the triangle: ", ar, "units sq.")
#
# import statistics as stat
# seq=[5,6,78,98,76,54]
# print(stat.mean(seq))
# print(stat.median(seq))
# print(stat.mode(seq))
# ######################################################################################
#
# # finding the leap year
# l = int(input('Enter year '))
# u=int(input("Enter final year "))
# for i in range(l, u+1):
#     if i % 4 == 0:
#         print(i, "is a leap year")
#     else:
#         print(i, "is not a leap year")
# # ------------------------------------------------------------------------------------------------------------#
# # finding even numbers
#
# l=int(input("Enter Ist number "))
# u=int(input("Enter IInd number "))
# for i in range(l,u+1):
#     if i%2==0:
#         print(i,"is an even number")
#     else:
#         print(i,"is not an even number")
# # ----------------------------------------------------------------------------------------------------------------#
#
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print('Current fruit :', fruits[1])
# # ======================================================#
#  find the sum of 1 to n using loop
# print("Hii,""Here u can find the sum of 'n' natural numbers")
# sum = 0
# n = int(input("Enter the number "))
# for num in range(1, n + 1):
#     sum = sum + num
#     print(sum)
# print("The sum is,", sum)
# ===========================================================================================#
#
# # find the multiples of a number
# mul=1
# n=int(input("Enter a number: "))
# for num in range(1,n+1):
#     mul=mul*num
# print("The multiple of the numbers is ", mul)
# # ===========================================================================================#
#
# n= int(input("upto whish natural number?: "))
# ctr=0
# sum_even=sum_odd=0
# while ctr<=n:
#     if ctr%2==0:
#         sum_even+=ctr
#     else:
#         sum_odd+=ctr
#     ctr+=1
# print("The sum of even integers is: ", sum_even)
# print("The sum of odd integers is: " ,sum_odd)
# # ========================================================================#
#
# a=b=c=0
# for i in range(1,21):
#     a=int(input("Enter number1: "))
#     b=int(input("Enter number2: "))
#     if b==0:
#         print("Divison by zero error! Aborting!")
#     else:
#         c=a//b
#         print("Quotient is=",c)
# print("Program over:)")
# # ____________________________________________________________________________________#
#
# x=int(input("Enter initial number: "))
# y=int(input("Enter final number: "))
# for i in range(x,y+1):
#     if i%2==0:
#         print(i,"is an even number")
#         continue
#     else:
#         print("odd number!")
# # =================================================================#
#
# # continue and break statements
# x=int(input("Enter initial number: "))
# y=int(input("Enter final number: "))
# for i in range(x,y+1):
#     if i%2==0:
#         print(i,"is an even number")
#         continue
#
# x=int(input("Enter initial number: "))
# y=int(input("Enter final number: "))
# for i in range(x,y+1):
#     if i%2==0:
#         print(i,"is an even number")
#         break
# # ==============================================================================================#
# # ==============================================================================================#
#
# l= int(input("Enter the lower limit: "))
# u= int(input("Enter upper limit: "))
# sum=0
# for i in range(l,u+1):
#     if i%2==0:
#         sum+=i
# print("The sum of even number is ",sum)
# # ======================================================================#
# sum=0
# l=1
# n=int(input("Enter the number:" ))
# for i in range(l,n+1):
#     sum+=i
# print("The sum of first" ,n, "natural number is ",sum)
#
# # ===================================================================================#
#
# flag concept
# l=[20,76,89,56,54]
# x=int(input("Enter the number u want to search: "))
# flag=0
# for i in l:
#     if i==x:
#         flag=1
#         print("The element is present")
#         break
# if flag==0:
#         print("The element is not present")
#
#
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# def fib(n):  # define a function for Fibonacci series
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2, n):  # gives value form 2nd number to 'n' value
#         c = a + b  # add values of 'a' and 'b'
#         a = b  # swaping the numbers
#         b = c
#         print(c)
#
#
# u = int(input("Enter number: "))  # number input from user
# fib(u)
# # -----------------------------------------------------------------------------------------------#
#
# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# for i in range(1,9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if(number_of_guesses>9):
#     print("Game Over")
# n=random.randrange(1,20)
# g=1
# print("The number of guesses are limited to 7 only" '\n')
# for i in range(1,7):
#     gn=int(input("Guess the number:"))
#     if gn>n:
#         print("You entered greater number, pls enter smaller number"'\n')
#     elif gn<n:
#         print("You entered smaller number, pls enter greater number" '\n')
#     else:
#         print("You won")
#         print(g,"number of guesses you took")
#         #break
#     print(7-g, "number of guesse are left" '\n')
#     g+=1
# if g>7:
#     print("Game over")

#
# num = int(input('enter'))
# mid = num//2
# print('the divisors of', num, 'are :')
# for i in range(2, mid+1):
#     if num%i==0:
#         print(i, end=' ', sep='and')



# sum of even numbers
'''l = int(input("Enter the lower limit: "))
u = int(input("Enter upper limit: "))
sum = 0
for i in range(l, u + 1):
    if i % 2 == 0:
        sum += i
print("The sum of even number is ", sum)
# ========================================================================

# sum of first n natural numbers
sum = 0
print("Hello programmers,\n"" here you can find the sum of 'n' natural numbers 😀")
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    sum += i
print("The sum of first", n, "natural number is ", sum)
# ========================================================================#

# finding number whether it is in the list or not
l = [11, 21, 65, 98, 35, 54, 98]
x = int(input("Enter the number u want to search: "))
flag = 1
for i in l:
    if i == x:
        flag = 2
        print("The element is present😀")
        break
if flag == 1:
    print("The element is not present😑")'''


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# program for Fibonacci series
# def fib(n):  # define a function for Fibonacci series
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2, n):  # gives value form 2nd number to 'n' value
#         c = a + b  # add values of 'a' and 'b'
#         a = b  # swaping the numbers
#         b = c
#         print(c)
#
#
# u = int(input("Enter number: "))  # number input from user
# fib(u)

'''import math

n=int(input("Enter a number: "))
sum=0
for i in range(1,n):
    sum+=i
print(sum)

l=["Na","Mg",'S','C','O','Ne']
x=str(input("Enter element u want to search: "))
p=1
for i in l:
    if i==x:
        p=2
        print("The element is present")
        break
if p==1:
    print("The element is not present: ")'''

# -----------------------------------------------------------------------------------------

# write a program to print the elements in the list with fir loop

'''l=["A", 'E', 'I', 'B', 'U', 'Y']
count=0
for i in l:
    j=i.upper()
    if j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
        count+=1
print("Number of vovels in the list are", count)'''

'''l = ['a', 'b', 'e', 'i', 'c', 'p', 'o', 'u']
count = 0
v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in range(0, len(l)):
    if l[i] in v:
        print("vovel found in ", i + 1,"th position")
        count += 1
print("The number of vovels are ", count)'''
# ----------------------------------------------------------------------------------------------------#

'''a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
if a<=0:
    b+=1
else:
    a+=1
if a>0 and b>0:
    print("w")
elif a>0:
    print("x")
if b>0:
    print("y")
else:
    print("z")'''
# ======================-----------==========------------================00000000-----------

'''count=sum=0
ans='y'
while ans=='y':
    num = int(input("enter a number: "))
    if num<0:
        print("number entered is less than zero, Aborting!")
        break
    sum+=num
    count+=1
    ans = input("Want to enyer more numbers? (y/n)")
else:
    print("You entered", count, "numbers so far")
print("Sum of numbers entered is", sum)'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

n=20
# g=1
# print("The number of guesses are limited to 7 only" '\n')
# for i in range(1,7):
#     gn=int(input("Guess the number:"))
#     if gn>20:
#         print("You entered greater number, pls enter smaller number"'\n')
#     elif gn<20:
#         print("You entered smaller number, pls enter greater number" '\n')
#     else:
#         print("You won")
#         print(g,"number of guesses you took")
#         #break
#     print(7-g, "number of guesse are left" '\n')
#     g+=1
# if g>7:
#     print("Game over")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# string= input("Enter a string: ")
# length=len(string)
# maxlen=0
# maxsub=''
# sub=''
# lensub=0
# for a in range(length):
#     if string[a] in"aeiou" or string[a] in "AEIOU":
#         if lensub>maxlen:
#             maxsub=sub
#             maxlength=lensub
#             sub=''
#             lensub=0
#     else:
#         sub+=string[a]
#         lensub=len(sub)
#     a+=1
# print("Maxmimun length consonant substring is: ", maxsub, end=" ")
# print("With", maxlen, "characters")
