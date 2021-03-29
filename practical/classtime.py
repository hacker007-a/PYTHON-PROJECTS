# string manipulation

# w = "Captain"
# print(w[1::-1])
# print(w[::-1])
# print(w.upper())

# w = "captainamerica"

# for i in (w):
#     print(i, end=' ')
# print()
#
# for i in range(0, len(w)):
#     print(w[i], end=' ')
# print()

# print(w+c)  # concatenation
# print(w+c*2)
# print("p" in w)
# print('p' not in w)  # membership
# print(len(w))
# print(w.upper('a'))
# print(w.capitalize())
# print(w.title())
# print(w.find("a"))
# print(w.count("a"))
# print(w.replace("a", "w"))
# print(w.isalnum())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# a= input("enter the word: ")
# u , l, d ,s=0,0,0,0
# for i in a:
#     if i.isupper()==1:
#         u+=1
#     elif i.islower() == 1:
#         l+=1
#     elif i.isdigit() == 1:
#         d+=1
#     else:
#         s+=1
# print("upper case", u,"\n" "lower case",l,"\n" "digit",d, "\n" "special characters",s)
#__________________________________________________________________________________________________

# Split function

'''s="welcome to school"
t=s.split("welcome to school")
print(s.split('o'))
print(s.split())
print(t)
print(len(t))

=s.lstrip()
print(c)
print(s)
b=s.rstrip()
print(b)
d=s.strip()
print(d,end=" ")
print("h")
a=s.replace('welcome','go')
print(s)
print(a)'''
# --------------------------------------------------------------------------------------------------------------#

# list in python

# l= [12,23,45,67,89,78,54,64]
# print(l)
# print(l.reverse())
# print(12 in (l))
# #print(len(l))
# for i in (l):
#     for j in (l):
#         print(i, end=' ')
# l.append(120)
# print(l)
# #l.insert(2,120)
# #print(l)
# x=int(input("Enter index value: "))
# y=eval(input("Enter the value"))
# l.insert(x,y)
# print(l)
# del l [3]
# print(l)
# ===============================================================
# s="welcome"
# s=list(s)
# print(s)
# l= [12,23,45,67,89,78,54,64]
# print(l)
# a=max(l)
# b=min(l)
# print("max =",a, "min =", b) ("max")
# l.pop(3)
# print(l)
# l.pop()
# print(l)
# l.remove(12)
# print(l)

#=====================================================================#
#
# a = ['marvel', 'dc', 'captain', 'vision', 'bucky']
# f=1
# x=input("Enter a character: \n")
# for i in a:
#     if i==x:
#         f=2
#         print('Character is present')
#         break
# if f==1:
#     print("Character not found")

#======================================================================#
# sum=0
# l=0
# u=int(input("To which number: "))
# sum_even=sum_odd=0
# for i in range(l,u+1):
#     if i%2==0:
#         sum_even+=sum
#     else:
#         sum_odd+=sum
#     sum+=1
# print("Sum of even numbers is ", sum_even )
# print("Sum of odd numbers is ", sum_odd)


# sum=0
# #l=int(input("From which number: "))
# u=int(input("Upto which number: "))
# sum_even=sum_odd=0
# while sum<=u:
#     if sum%2==0:
#         sum_even+=sum
#     else:
#         sum_odd+=sum
#     sum+=1
# print("Sum of even numbers is ", sum_even )
# print("Sum of odd numbers is ", sum_odd)
#============================================================#
#
# l=[1,54,98,7,86,75,4567,983,112,907,564,785]
# print('initial list=',l)
# # for i in l:
# #         print(i)
# # print()
# l.pop(4)
# print("poped out",l)
# l.append(4)
# print('appended',l)
# l.insert(2,2)
# print('inserted',l)
# del l [6]
# print('deleted', l)

#============================================================#

# a=(input("Enter any string "))
# u,l,d,s=0,0,0,0 #l=lower case, u=upper case, d=digt, s=special character
# for i in a:
#     if i.isupper()==1:
#         u+=1
#     elif i.islower()==1:
#         l+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         s+=1
# print("Upper case: ", u,'\n' 'Lower case: ',l,'\n' 'Digits: ',d,'\n' 'Special char: ',s)
#=========================================================================#

#t1 = (10,20,30,5,6,40,50,60,60,60,70)
# t2 = 60,70
# min=t1[0]
# max=t1[0]
# for i in t1:
#     if i<min:
#         min=i
# print("min value", min)
#
# for i in t1:
#     if i>max:
#         max=i
#
# print("max value", max)
# print(type(t1))
# print(len(t1))
# print(t1[1][0])
# for i in t1:
#     if i%3==0:
#         print(i)
# print(type(t))
# print(len(t))
# for i in range(0, len(t)):
#     print(t[i])
#
# t3 = t1+t2
# print(t3)
# t1 = (10,20,30,5,6,40,50,60,70)
# x = int(input('enter a number: '))
# flag = 0
# for i in t1:
#     if i==x:
#         flag=1
#         print('number found')
# if flag==0:
#     print('the number not found!')
#
#
#
# # else:
# #     print('present',flag, 'times')
#---------------------------------------------------------------------------------------------------------------------#

# dictionary

# dict = {'a':1000, 'b':2000, 'c':3000}
# print(dict)
# for i in d:
#     print(i)
# for i in d.values():
#     print(i, end='')
#     print()
# for i in d.keys():
#     print(i, end='')
#     print()

# year = {'jan':31, 'feb':28, 'mar':31}
# x=input('enter the month: ')
# flag = 0
# for i in year:
#     if i==x:
#         flag=1
#         print('the no of days in month is', year[i])
# if flag==0:
#     print('enter valid month')

# s ="india"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#
#     else:
#         d[i]=1
# print(s.upper())
# print(d)

# update() important

# d = {'january':31, 'feb':28, 'march':31}
# print(d)
# d1 = d.update(feb=29)
# d2 = d.update(apr=30)
# print(d)
# del d['january']
# print(d)


# key = {1,2,3,4,5}
# value = 'number'
# dic = dict.fromkeys(key , value)
# print(dic)

# import numpy as np
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
# print(x)
# print(y)

# d = {'ri':[12,14], 'wa':[2,16], 'qs':[10,15]}
# x = input('enter the name: ')
# flag=0
# for i in d:
#     if i==x:
#         flag=1
#         print('name found', i)
#         print('the details are ', d[i])
#
# if flag==0:
#     print('name not in the list')

# d = {}
# while True:
#     name = input("enter name: ")
#     age = int(input('Enter age: '))
#     roll = int(input('enter roll no: '))
#     d[name]=[roll, age]
#     choice = input('do u want to enter more(y/n)')
#     if choice=='n' or choice=='N':
#         break
#
# print(d)
#==========================================================================================#

# functions and modules    (25/1/21)

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 100)
#
# # Plot the data
# plt.plot(x, x, label='hyperbola')
#
# # Add a legend
# plt.legend()
#
# # Show the plot
# plt.show()


# ------------------------------------------------------------------------------------------------------------

# tup = eval(input('enter a tuple: '))
# if sorted(tup, reverse = False) == list(tup):
#     print('tuple is sorted')
# else:
#     print('tuple not sorted')
#

# mks = eval(input('enter marks: '))
# total = sum(mks)
# avg = total/5
#
# if avg>=75:
#     grade='A'
# elif avg>=60:
#     grade = 'B'
# elif avg>=50:
#     grade='C'
# else:
#     grsde='D'
#
# print('Total marks is ',total, '\n' "average: ", avg, '\n' "Grade: ", grade, '\n')
#

# import json
# sent = "I am the best"
# words=sent.split()
# d= {}
# for i in words:
#     key = i
#     if key not in d:
#         count=words.count(key)
#         d[key]=count
#
# print('counting frequencies in list \n', words)
# print(json.dumps(d, indent = 1))

# s=" welcome to my        gfr "
# print(s.lstrip())
# print(s.strip()


# b=[2,5,13,15,8]
# c=[]
# for i in b:
#     if i%5==0:
#         print()

# list = [12,35,46,78,98,67]
# n = int(input("Enter the number: "))
# flag = 0
# for i in list:
#     if i == n:
#         flag=1
#         print('numbert is present')
#
# if flag==0:
#     print('number is not present')
#
# s=str(n)
# c=n.count(s)
# print(c)


d = {1:'monday', 2:'tuesday',3:'wednesday',4:'thursday'}
print(d.keys())























