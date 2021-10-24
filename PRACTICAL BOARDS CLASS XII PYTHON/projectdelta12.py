# read a text file line by line and display each word seperated by a '#'

# def wordread():
#     f = open('quote.txt', 'r')
#     lines = f.readlines()
#     for line in lines:
#         # print(line, end='')
#         words = line.split()
#         for i in words:
#             print(i+'#', end='')
#         print()
# f.close()
# wordread()

# def wordread():
#     f = open('quote.txt', 'r')
#     while True:
#         lines = f.readline()
#         if lines == '':
#             break
#         else:
#             words = lines.split()
#             for i in words:
#                 print(i+'#', end='')
#             print()


# wordread()
#--------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------#

#Create a binary file with name and roll no. search for a given roll number and display the name if not found display appropriate msg

# import pickle

# def write():
#     f = open('details.dat', 'wb')
#     while True:
#         r = int(input('Enter Roll no.: '))
#         n = input('Enter name: ')
#         data = [r,n]
#         pickle.dump(data, f)
#         ch = input('Do you want to enter more?(Y/N :')
#         if ch in 'Nn':
#             break

#     f.close()

# # now search for given roll no.
# def search():
#     found = 0
#     rollno = int(input('Enter roll no. whose name you want to display: '))
#     f = open('details.dat', 'rb')
#     try:
#         while True:
#             rec = pickle.load(f)
#             if rec[0] == rollno:
#                 print(rec[1])
#                 found = 1
#                 break

#     except EOFError:
#         f.close()
#     if found == 0:
#         print('Sorry..No record found')
#     f.close()

# write()
# search()

# def writedet():
#     f = open('student.dat','wb')
#     while True:
#         dic = {}
#         r = int(input('Enter Roll No.: '))
#         n = input('Enter Name: ')
#         dic['Rollno.'] = r
#         dic['Name'] = n
#         pickle.dump(dic, f)
#         ch = input('Do you want to enter more?(Y/N): ')
#         if ch in 'Nn':
#             break
#     f.close()

# def searchdet():
#     found = 0
#     rn = int(input('Enter roll no. you want to search: '))
#     f = open('student.dat', 'rb')
#     try:
#         while True:
#             rec = pickle.load(f)
#             if rec['Rollno.'] == rn:
#                 print(rec['Name'])
#                 found = 1
#                 break

#     except EOFError:
#         f.close()
#     if found == 0:
#         print('Record not found...')
#     f.close()

# # writedet()
# searchdet() 




