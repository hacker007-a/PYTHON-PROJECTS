# ########################################################################################################
# ########################################################################################################
#
# # PRACTICALS FOR CS
#
# # 1. INPUT WELCOME MESSAGE
# wel = input('Enter welcome message:- ')
# print(wel.title())
#
#
# # 2. Input two numbers and display the larger / smaller number.
# num1 = float(input('Enter Ist number: '))
# num2 = float(input('Enter IInd number: '))
# if num1 > num2:
#     print('The larger number is', num1)
# elif num2 > num1:
#     print(num2, 'is larger number:')
#
#
# # 3. Input three numbers and display the largest / smallest number.
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2st number: "))
# num3 = float(input("Enter 3st number: "))
# if (num1>num2) and (num1>num3):
#     largest = num1
#     print('The largest number is ', largest)
#
# elif (num2>num1) and (num2>num3):
#     largest = num2
#     print('The largest number is ', largest)
#
# else:
#     largest = num3
#     print('The largest number is ', largest)
#
# #----------------------------------------------------------------------------------------------------
#
# # 4.Take a number from user,and print the factorial of the number,
# # also check whether the number is prime or not.
#
# num = int(input('Enter a positive number: '))
# fac = 1
# for i in range(1, num+1):
#     fac *= i
# print('The factorial of ', num, 'is', fac)
# for i in range(2, num):
#     if num % i == 0:
#         print('Then number is a composite number')
#         break
# else:
#     print('The number', num, 'is a prime number')
#
# # -----------------------------------------------------------------------------------------------------------
#
# # 5.Take a number from user and check whether the the number is Armstrong number or not
# # also check whether the number is divisible by n or not.[n to be taken from user]
#
# print('*Check whether a number is armstrong number and not')
# num = int(input('Enter number: '))
# sum = 0
# wnum = num
# while wnum > 0:
#     digit = wnum % 10
#     sum += digit**3
#     wnum //= 10
# if num == sum:
#     print(num, 'is an armstrong number')
# else:
#     print(num, 'is not an armstrong number')
#
# print("Checking the divisibility of the number", num, '\n''with the user given number')
# n = int(input('Enter the number: '))  # checking the divisibility of the number
# if num % n == 0:
#     print('The number', num, 'is divisible by', n)
# else:
#     print('The number', num, 'is not divisible by', n)
#
# # -------------------------------------------------------------------------------------------
#
# #6.Create a list and do the following:-
#
# lst = [2, 12, 43, 65, 78, 98, 54, 90, 99, 121, 44]

# print('The list is', lst)
# n = lst[-1]
# print('The last element of  the list is', n)
#
# # ii)Print all the odd numbers from the list.
# only_odd = [num for num in lst if num % 2 == 1]
# print('Odd numbers: ', only_odd)
#
# # iii)Print the sum of all even numbers from the list.
# only_even = [num for num in lst if num % 2 == 0]
# print('Even numbers: ', only_even)
# sum = sum(only_even)
# print('Sum of even numbers in the list is', sum)
#
# # iv)Check whether a number is present in the list or not.
# # [take the number from user]
# n = int(input('Enter number you want to find: '))
# flag = 0
# for i in lst:
#     if i == n:
#         flag = 1
#         print('The number is present in list')
#
# if flag == 0:
#     print('Number is not in the list')
#
# # -------------------------------------------------------------------------------
#
# # 7.Take a sentence as input from user and do the following:-
# # i)Find out the number of uppercase,lowercase chars,and numbers from the string.
# word = input('Enter a string: ')
# upper, lower, chars, digit = 0, 0, 0, 0
# for str in word:
#     if str.isupper()==1:
#         upper += 1
#     elif str.islower()==1:
#         lower+=1
#     elif str.isdigit()==1:
#         digit += 1
#     else:
#         chars += 1
# print('Upper case: ', upper, '\n', 'Lower case: ', lower, '\n',
#       'Digits: ', digit, '\n', 'Special characters: ', chars)
#
# # ii)Remove the left hand side spaces from the string(if any).
# print('String after removing leading whitespace', word.lstrip())
#
# # iii)Find out number of words in the sentence.
# count = len(word)
# print('Length of the word is: ', count)
#
# #---------------------------------------------------------------------------------------
#
#
# # 8.Take a tuple from user and do the following:-
# # i)Print the average of all the elements of tuple.
#
# tup = eval(input('Enter a tuple: '))
# length = len(tup)
# sum = avg = 0
# for i in range(0, length):
#     sum += tup[i]
#     avg = sum/length
# print('Given tuple is:', tup)
# print('Average of the tuple is: ', avg)
#
# # ii)Print the tuple in reversed order.
# print('Tuple in reversed order: ', tup[::-1])
#
# # ---------------------------------------------------------------------------------------
#
# # 9.Create a dictionary with class name and number of students as key and value pair,
# # then accept class name from user and print matching number of student.
#
# dic = {'VI': 40, 'VII': 34, 'VIII': 34, 'IX': 35, 'X': 40, 'XI': 23, 'XII': 25}
# print(dic)
# cls = input('Enter class name in Roman numeral: ')
# for i in dic:
#     if i == cls:
#         print('Number of students: ', dic[i])

# ----------------------------------------------------------------------------------------

# 10.Create a dictionary with employee name and salary of employee,
# and take user name as input and print the salary.
# employees = {'Akash': {'salary': 15000}, 'Mohit': {'salary': 15000}, 'Steve': {'salary': 21000},
#             'Prakash':{'salary': 22000}, 'Divya': {'salary': 21000}}
employees = {'Akash':15000}
# user_name = input("Enter employee name: ")
# for i in employees:
#     if user_name in i:
#         print('Salary is: ', employees[i])
#         # print('Salary is', (employees[i]['salary']))


