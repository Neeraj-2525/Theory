# FILE HANDLING
# f = open('Neeraj.txt', 'r')
# str1 = f.read()
# print(str1)
# f.close()
# str2 = f.read()
# print(str2)

# f = open('Neeraj.txt', 'w')
# f.write('Hello this is the updated content')
# f = open('Neeraj.txt', 'r')
# print(f.read())

# f = open('Neeraj.txt', 'a+')
# f.write('\nHello this is the updated content\n')
#
# f = open('Neeraj.txt', 'r')
# print(f.read())
# f.close()

# f = open('Neeraj.txt', 'r')
# print(f.readline())        # read a single line
# print(f.readline())
# print(f.readlines())       # read multiple lines

# with open('Neeraj.txt', 'r') as f:
#     print(f.read())         # closes file automatically

# with open('Neeraj.txt', 'a') as f:
#     f.write('\nThis is the updated line2\n')

# with open('Neeraj.txt', 'r') as fIlE:
#     print(fIlE.readlines())

# To add item of a list in the file
# fruits = ['apple', 'mango', 'raspberry']
# with open('Neeraj.txt', 'w') as f:
#     for i in fruits:
#         f.write(i+'\n')

# To read file line by line
with open('Neeraj.txt', 'r') as f:
    count = 0
    for lines in f:
        if lines % 3 == 0:
            count += 1
            print(lines)


