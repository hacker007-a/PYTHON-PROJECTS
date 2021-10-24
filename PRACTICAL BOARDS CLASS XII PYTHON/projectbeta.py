# Create a csv file by entering user-id and password, read and search the password for given user id.

# import csv
# def writecsv():
#     f = open('Credentials.csv', 'w', newline='')
#     wo = csv.writer(f)
#     wo.writerow(['Username', 'Password'])
#     while True:
#         uid = input('Enter user id: ')
#         pswd = input('Enter password: ')
#         data = [uid, pswd]
#         wo.writerow(data)
#         ch = input('Do you want to enter more records(Y/N): ')
#         if ch in 'Nn':
#             break

#     f.close()

# def readcsv():
#     f = open('Credentials.csv', 'r')
#     ro = csv.reader(f)
#     for i in ro:
#         print(i)
#     f.close()


# def searchcsv():
#     f = open('Credentials.csv', 'r')
#     found = 0
#     u = input('Enter user id to display password: ')
#     ro = csv.reader(f)
#     next(ro)

#     for i in ro:
#         if i[0] == u:
#             print(i[1])
#             found = 1
#     if found == 0:
#         print('No record Available....')    
#     f.close()

# # writecsv()
# # readcsv()
# searchcsv()

#*********************************************************************************************************

# Remove all the lines that contain the character 'a' in a file and write it to another file

def remove():
    f = open('sampletext.txt', 'r')
    lines = f.readlines()
    # print(lines)
    fo = open('sampletext.txt', 'w')
    fn = open('samplenewtext.txt', 'w')
    for line in lines:
        if 'a' in line:
            fn .write(line)
        else:
            fo.write(line)
    print('Data updated sucessfully..')
    fo.close()
    fn.close()

remove()