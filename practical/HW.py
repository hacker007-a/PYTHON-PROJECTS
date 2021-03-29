# # dictionary practice
#
# m = {}
# n = int(input('How many students '))
# for i in range(n):
#     r,p=eval(input('Enter roll number, Marks:'))
#     m[r]=p
# print('Created dictionary')
# print(m)
#
# dic = {1:100, 2:2000, 3:300, 4:400}
# print(dic)
# print(dic.keys())
# print(dic.values()

# m = {}
# n = int(input('how many students '))
# for i in range(n):
#     r, p = eval(input('Enter roll number, Marks:'))
#     m[r]=p
# print('Created dictionary')
# print(m)
# # ans = 'y'
# ans = input('more students? (y/n): ')
# while ans=='y':
#     print('enter details of new students:')
#     r, p = eval(input('Enter roll number, Marks:'))
#     m[r] = p
#     ans = input('more students? (y/n): ')
#     print('dict after adding new student')
#     print(m)
#
# n=int(input('how many students: '))
# compwinners = {}
# for i in range(n):
#     key = input('name of the student: ')
#     value = int(input('number of comp won: '))
#     compwinners[key]=value
#
# print("the dict now is")
# print(compwinners)
#===================================================================================================#

# to find whether the numbr is palindrom or not
#
# num = int(input('Enter a number: '))
# wnum = num
# rev = 0
# while wnum>0:
#     dig = wnum%10
#     rev = rev*10+dig
#     wnum = wnum//10
# if num==rev:
#     print('Number', num, 'is a palindrome')
# else:
#     print('Number', num, 'is not a palindrome')

#==========================================================================================================#

#tuple manipulation

# tup=eval(input('Enter a tuple: '))
# for i in tup:
#     if tup.count(i)>1:
#         print('Contains duplicate elements')
#
#     else:
#         print("does not contain duplicate")
#
#         break

# to find the second largest number

# T=(23,45,54,98,768,654,987)
# maxvalue=max(T)
# length=len(T)
# secmax=0
# for i in range(length):
#     if secmax<T[i]<maxvalue:
#         secmax=T[i]
# print('second largest number is', secmax)
####################################################################


# username, domaain name and email list with tuple
#
# lst=[]
# n=int(input('How many students: '))
# for i in range(1, n+1):
#     email=input('Enter email id of the student' + str(i) + ':')
#     lst.append(email)
#     etuple=tuple(lst)
#
# lst1 = []
# lst2 = []
# for i in range(n):
#     email = etuple[i].split('@')
#     lst1.append(email[0])
#     lst2.append(email[1])
#
# unametup = tuple(lst1)
# dnametup = tuple(lst2)
#
#
# print("student email id's")
# print(etuple)
# print('UserName tuple')
# print(unametup)
# print('domain name tuple')
# print(dnametup)

########################################################################################################
########################################################################################################

# Trick 10: You can also  write: print(name == name[ : : -1])
# And one bonus trick: one can check odd even using just  this line
# print('odd' if int(input('Enter a number: '))%2 else 'even')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
######################################################################################################


# 3. Given two integers x and n, compute x**n

# from math import pow
# x = float(input("Enter a positive number: "))
# n = int(input('Enter the power of the number: '))
# power = pow(x,n)
# print('The number',x , 'raised to the power', n, 'is', power)


# 4(1). Write a program to input the value of x and n and print the sum of the
# following series
# 1+x+x2+x3+x4+.............x**n

# x = float(input('Enter value of x: '))
# n = int(input('Enter value of n (fand x**n): '))
# s=0
# fand num in range(n+1):
#     s += x**num
# print('Sum of first', n, 'terms:', s)


# 1-x+x2-x3+x4-.............xn

# x = float(input('Enter value of x: '))
# n = int(input('Enter the power(n): '))
# s=0
# sign = +1
# fand i in range(n+1):
#     term = (x**i)*sign
#     s += term
#     sign *= -1
# print('Sum of first', n, 'terms:', s)


# x+x^2/2!-x^3/3!+x^4/4!-....x^n/n!

# x = int(input('Enter value of x: '))
# n = int(input('Enter the power (n): '))
# s = x
# sign = +1
# fand a in range(2, n+1):
#     f = 1
#     fand i in range(1, a+1):
#         f *= i
#     term = ((x**a)*sign)/f
#     s += term
#     sign = -1
#
# print('Sum of first',n, 'terms: ', s)


# 5 Determine whether a number is a perfect number, an armstrong number and a palindrome.
# # palindrom number


# print("*Check whether a number is a palindrom number and not")
# num = int(input('Enter number: '))
# wnum = num    # working numbers stores num initially
# rev = 0
# while (wnum>0):
#     dig = wnum%10
#     rev = rev*10+dig
#     wnum = wnum//10
# if (num==rev):
#     print('Number', num, 'is a palindrom')
# else:
#     print('Number', num, 'is not a palindrom ')
#
#
#
# # perfect number
# print('*Check whether a number is a prfect number and not')
# n = int(input('Enter number: '))
# sum = 0
# fand i in range(1,n):
#     if (n%i==0):
#         sum+=i
# if (sum==n):
#     print('The number', n, 'is a perfect number')
# else:
#     print('The number', n, 'is not a perfect number')


# 7 Display the terms of a Fibonacci series.

# t = int(input("Upto how many terms: "))
# a = 0
# b = 1
# print('Fibonacci series is ')
# print(a,",",b, end = ', ')
# fand i in range(2, t):
#     c = a+b
#     a = b
#     b = c
#     print(c, end = ', ')


# 9 Count and display the number of vowels, consonants, uppercase, lowercase
# characters in string.

# str=input("Please enter a string as you wish: ")
# vowels, consonants, upper, lower  = 0,0,0,0
# for i in str:
#     if(i == 'a'and i == 'e'and i == 'i'and i == 'o'and i == 'u' and
#        i == 'A'and i == 'E'and i == 'I'and i == 'O'and i == 'U' ):
#            vowels += 1
#     else:
#         consonants += 1
# for i in str:
#     if i.isupper() == 1:
#         upper += 1
#     elif i.islower() == 1:
#         lower += 1
# print('Upper case ', upper)
# print('Lower case ', lower)
# print('Vowels are ', vowels)
# print('Consonants are', consonants)


# 10 Input a string and determine whether it is a palindrome and not;
# convert the case of characters in a string.

# str = input("Enter a string: ")
# rev = str[::-1]
# for i in str:
#     if str == rev:
#         print("The wandd is a palindrome")
#         break
# else:
#     print('Not a Palindrome!')


# 11 Find the largest/smallest number in a list/tuple

# lst = eval(input("Enter a list: "))
# print('The list is ', lst)
# max = max(lst)
# min = min(lst)
# print('Largest number in this lis is', max)
# print('Smallest number in the list is', min)


# 12 Input a list of numbers and swap elements at the even location
# with the elements at the odd location.
#
# val = eval(input('Enter a list : '))
# print("Original List is:", val)
# s = len(val)
# if s%2!=0:
#     s-=1
# for i in range(0,s,2):
#     val[i],val[i+1]=val[i+1],val[i]
# print("List after swapping :",val)


# 13 Input a list/tuple of elements, search for a given element in the list/tuple.
#
# lst = eval(input('Enter the list: '))
# f = int(input('Enter the elemment you want to search for: '))
# flag = 0
# for i in lst:
#     if i == f:
#         flag = 1
#         print('Element', i,'is present in list'  )
#         break
#
# if flag == 0:
#     print('Element is not present in list')


# 14 Input a list of numbers and test if a number is equal to the sum of the cubes of
# its digits. Find the smallest and largest such number from the given list of
# numbers.

# 15 Create a dictionary with the roll number, name and marks of n students in a
# class and display the names of students who have marks above 75.
#
# cls = {}
# while True:
#     roll_no = int(input("Enter roll number: "))
#     name = input("Enter Student's name: " )
#     marks = int(input('Enter the marks: '))
#
#     cls[roll_no] = [name, marks]
#     choice = input('Do you want to enter more? (y/n): ')
#     if choice == 'n' or choice == 'N':
#         break
# print(cls)
#
# for student in cls:
#     if cls[student][1] > 75:
#         print('student',cls[student][0], 'scored marks above 75')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# --------------------------------------------------------------------------------------------------


# emp = {'Sandi': {'salary': 32000}, 'Yadav': {'salary': 23000}, 'Launda': {'salary': 20000}}
# un = input('Enter employee name: ')
# for i in emp:
#     if un in i:
#         print('Salary is:', (emp[i]['salary']))


# cls = {'IX': {'students': 45}, 'X': {'students': 43}, 'XI': {'students': 23}}
# name = input('Enter class name in roman numeral: ')
#
# for i in cls:
#     if name in i:
#         print('Number of students : ', (cls[i]['students']))

#
# tup = eval(input('Enter tuple'))
# length = len(tup)
# sum = avg = 0
# for i in range(0, length):
#     sum+=tup[i]
#     avg = sum/length
# print(avg)
# print(tup[::-1])
#
# print(12+32+56/3)
# print(100/3)


# num1 = float(input('enter number:'))
# num2 = float(input('enter number:'))
# num3 = float(input('enter number:'))
# if (num3>num1) and (num2<num3):
#     print('great', num3)
#
# elif num2>num3 and (num1<num2):
#     print('great', num2)
# else:
#     print('great', num1)


# n = int(input('enter number:'))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
# for i in range(2, n):
#     if n%i == 0:
#         print('composite')
#         break
# else:
#     print('prime')

#
# n=int(input('enter number:'))
# wnum = n
# sum = 0
# while wnum>0:
#     digit = wnum%10
#     sum += digit**3
#     wnum//=10
# if n==sum:
#     print('armstrong')
# else:
#     print('not armstrong')




# print(507%10)
# print(507/10)
# print(507//10)


# num = input("Enter the number: ")
# lst = []
# for c in num:
#     lst.append(int(c)**int(len(num)))
#
# if sum(lst) == int(num):
#     print("This number is a armstrong number")
#
# else:
#     print("This number is not a armstrong number")


# num = input('enter number: ')
# lst = []
# for i in num:
#     lst.append(int(i)**len(num))
# if sum(lst) == int(num):
#     print('yes')
#
# else:
#     print('no')

#
# s = input('enter')
# print('replaced')
# print(s.replace(' ', '-'))


# d = {1:34, 2:35, 3:36}
# seq = d.keys()
# g = d.get(1)
# f = d[1]
# print(g)
# print(f)
# print(seq)
# v = d.values()
#  print(v)


# print(12|13)
# print(~12)
# print(12 or 13)
# print('bin of 12',bin(12))
# print('bin of 13',bin(13))
num = int(input('enter:'))
for i in range(2,num):

    if num % i == 0:
        print('composite')
        break
else:
    print('prime')