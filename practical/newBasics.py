# open, read, and readline
# f = open('hello.txt', 'rt')
# cont = f.read(2) # read the characters
# cont = f.read() # read the whole content
# print(cont)

#
# f.close()
# for line in f:
# print(line, end = '') # print every line, but first do not
# put read function before

# print(f.readline()) # print first line
# print(f.readline()) # print second line with a newline char
# print(f.readlines())  # print a list of the file
###################################################################################################################
###################################################################################################################

# Writing and appending to a file

# f = open('hello.txt', 'w') # open a file in write mode, 'a' will append
# f.write('I am good\n')
# # f.close()
# a = f.write('I am good\n')
# print(a) # print number of characters in the file


# f = open('hello.txt', 'r+') # open a file in write mode, 'a' will append
# print(f.read())
# f.write('thank u')
############################################################################################
############################################################################################

# seek(), tell(), more operations on file

# f = open('hello.txt')
# f.seek(11)
# print(f.tell())
# # print(f.readline())
# # print(f.tell()) # tell the file pointer position at which char
# print(f.readline())
# # print(f.tell())
# f.seek(11) # will seek the starting line to read at input position
# print(f.readline())
# f.close()
##############################################################################
##############################################################################

# using 'with block' to open python file
# f = open('hello.txt')
# # same work as pointer f, automatically close the file
# with open('hello.txt') as f:
#     a = f.readlines()
#     print(a)
#
# f = open('hello.txt')
# b = f.readlines()
# print(b)

#####################################################################
#####################################################################

# global variables and keywords
# l = 10 # global variable: scope
# def func1(n):
#     # l = 5 # local variable
#     global l # can change the global var inside the function
#     l += 7 # local var can be resolved, but global cant
#
#     print(l)
#     print(n, 'I have printed')
#
# func1('this is me')
# x = 89
# def ash():
#     x = 20
#     def big():
#         global x #this will go outside the function and search for the global var
#         x = 88 # and make this as global var
#     # print('before "big"', x)
#     big()
#     print('after "big"',x)
# ash()
# print(x)
##########################################################################################
##########################################################################################

# Lambda functions or anonymous functions

# minus = lambda x, y: x - y # Creates a function without def()
# print(minus(9,5))
# def a_first(a):
#     return a[1]

#
# a = [[1,14],[5,6], [8,23]]
# a.sort(key=lambda x:x[1]) # key is an argument which takes function as input
#
# print(a)
#############################################################################################
#############################################################################################

# Using built in & external module
#
# import random
# # num = random.randint(0,67)
# # # print(num)
# # rand = random.random()*100
# # print(rand)
# lst = ['hii', 'hello', 'movies', 'get', 'justiceLeague', 'falcon']
# r = random.choice(lst)
# print(r)
#############################################################################################
#############################################################################################

# 'f' string and string formatting
# me = 'Ashking'
# a1 = 7
# a = 'This is {1} {0} '
# b = a.format(me, a1)
# print(b)
# a = f'this is {me} {a1}'
# print(a)

##############################################################################
#################################################################################

# time module in python

# import time
# initial = time.time() # retrns ticks in sec
# # print(initial)
# k = 0
# while k<45 :
#     print('hello')
#     time.sleep(1) # print char after 1 sec of interval
#     k+=1
# print('while loop runtime = ', time.time() - initial, 'sec')
# # print execution time of the programe
#
# initial2 = time.time()
# for i in range(45):
#     print('Hello')
# print('for loop runtime = ', time.time()-initial2,'sec')

# din = time.asctime(time.localtime(time.time()))
# print(din)
# asctime- returns the tiime value from tuple
# time.time - returns ticks

############################################################################################
############################################################################################

# Enumerate function
l1 = ['ghy', 'dfg', 'sf', 'blackcat']

# i = 1
# for item in l1:
#     if i%2 != 0:
#
# #     i+=1
# for index, item in enumerate(l1): #returns index as well as item in the list
#     if index % 2==0:
#         # print(f'Jarvis please take {item}') #same
#         print('Jarvis please take', item)
#
# from playsound import playsound
# m = playsound('C:\\Users\\Ashu\\Downloads\\dl\\ChipGenius_v4_20_1107_fix\\mlg\\06 - Ho Ja Mast Malang Tu - Malang 2020.mp3')
# playsound(m)

####################################################################################################################
####################################################################################################################

# args & kwargs

# def func(normal, *args, **kwargs):  # any name can be given
#     # priority - normal argument>*args>*kwargs
#     print(nor)
#     for item in args:
#         print(item)
#
#     for key, value in kwargs.items():
#         print(f'{key} is a {value}')
#
#
# nor = 43
# hay = ['captain', 'thor', 'ironman', 'batman', 'deathstroke']
# # func(*hay) # it means tha all the arguments in the list is passed t the function and is stored as tuple in UDfunction
#
# kw = {'captain':'leader', 'man':2, "norb":3,'aqua': 'water'}
# func(*hay,**kw)

########################################################################################################################
########################################################################################################################

# Recursions Recursive Vs Iterative approach
#
# def factorial_iterative(n):
#
#         fac = 1
#         for i in range(n):
#             fac*=i+1
#         return fac
#
#
# num = int(input('Enter number: '))
# print('Iterative',factorial_iterative(num))


# def factorial_recursive(n):
#     if n == 1:
#         return 1
#
#     else:
#         return n * factorial_recursive(n - 1)
# if n=5
# 5* factorial_recursive(4)
# 5*4*factorial_recursive(3)
# 5*4*3*factorial_recursive(2)
# 5*4*3*2*factorial_recursive(1)
# factorial_recursive(1) will be returned as 1
# 5*4*3*2*1 = 120

#
# num = int(input('Enter number: '))
# print('recursive', factorial_recursive(num))

# def fibonacci(n):  # -:example
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
#
# num = int(input('Enter no of terms: '))
# print(fibonacci(num))                                  # 0,1,1,2,3,5,8,13

####################################################################################################################
####################################################################################################################

# if __name__ ==__main__

# def printstr(string):
#     return f'This is the string {string}'
#
#
# print(printstr('hii every'))


# if __name__ == '__main__':  # execute only the function needed in other file , not the whole content of the file in
    # which functions are provided

####################################################################################################################
####################################################################################################################

# Join function in Python

# hay = ['captain', 'thor', 'ironman', 'batman', 'deathstroke']
# a = ', '.join(hay)
# print(a)

######################################################################################################################
######################################################################################################################

# map, filter
# map- applies a function into whole list

# num = ['1', '3', '5', '8']
# ny = list(map(int, num))   # returns the list of the numbers of map
# print(ny)
# for i in range(len(num)):
#     num[i] = int(num[i])
# num[2]+=1
# print(num[2])

# n = [1,2,3,4,5]
# squ = list(map(lambda x: x*x, n))
# print(squ) # returns square of the numbers in the list

# def square(a):
#     return a*a
#
#
# def cube(a):
#     return a*a*a
#
#
# func = [square, cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)     # a function which with input x, returns function name(x) and its value(i)



# lst = [1,2,3,4,5,6,7,8]
#
# def is_greater(num):
#     return num>5
#
#
# grt_5 = list(filter(is_greater, lst)) #filters the numbers from the list which is greater than 5
# print(grt_5)


# from functools import reduce
# lst = [1,2,3,4,5]
# # num = 0
# # for i in lst:
# #     num+=i
# # print(num)
#
# num = reduce(lambda x,y: x+y, lst)
# print(num)

####################################################################################################################
####################################################################################################################

# Decorators
# def funcret(num):
#     if num == 0:
#         return print
#
#     if num == 1:
#         return sum
#
#
# a = funcret(1)
# print(a)
#
#
# def executor(func):
#    func('this')
#
#
# executor(print)


# def dec1(func):
#     def nowexe():
#         print('Executing')
#         func()
#         print('Executed')
#
#     return nowexe
#
#
# @dec1 # decorator
# def amigood():
#     print('hii')
#
# amigood()
#
#######################################################################################################################
#######################################################################################################################

# Advanced programming










