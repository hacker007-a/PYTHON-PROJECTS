# read a text file and display the numbers vovels,consonants, uppercase, lowercase characters

# def countVCUL():
#     f = open('report.txt', 'r')
#     v=c=u=l=n=s=0
#     data = f.read()
#     for i in data:
#         if i.isalpha():
#             if i.isupper():
#                 u+=1
#             if i.islower():
#                 l+=1
#             if i in 'aeiouAEIOU':
#                 v+=1
            
#             else:
#                 c+=1
#         # elif i.isdigit():
#         #     n+=1
#         # else:
#         #     s+=1

#     print('Vowels: ', v)
#     print('Consonants: ', c)
#     print('Uppercase: ', u)
#     print('Lowercase: ', l)
#     # print('Numeric: ', n)
#     # print('Special: ', s)
    
# countVCUL()

######################################################################################################

#Create a binary file with roll no, name, and marks. input a roll number and update the marks.

# from os import close, truncate
# import pickle
# def write():
#     f = open('studentdetails.dat', 'wb')
#     while True:
#         r = int(input('Enter Roll no.: '))
#         n = input('Enter Name: ')
#         m = int(input('Enter marks: '))
#         file = [r,n,m]
#         pickle.dump(file, f)
#         ch = input('Do you want to enter more?(Y/N): ')
#         if ch in 'Nn':
#             break
#     f.close()

# def read():
#     f = open('studentdetails.dat', 'rb')
#     try:
#         while True:
#             rec = pickle.load(f)
#             print(rec)
#     except EOFError:
#         f.close()

# def update():
#     f = open('studentdetails.dat', 'rb+')
#     rollno = int(input('Enter roll no. whose marks you want to update: '))
#     found = 0
#     try:
        
#         while True:
#             pos = f.tell()
#             rec = pickle.load(f)
#             if rec[0] == rollno:
#                 um = int(input('Enter updates marks: ')) 
#                 rec[2]=um
#                 f.seek(pos)
#                 pickle.dump(rec,f)
#                 found = 1
#                 print('Record Updated.')
                
#     except EOFError:
#         f.close()
#     if found == 0:
#         print('Record not found...')


# # write()
# read()
# update()
# read()
