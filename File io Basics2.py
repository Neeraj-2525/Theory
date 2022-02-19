# f = open("break and continue.py","w")
# f.write("Neeraj bhai bohot achha hai")
# f.close

# f = open("break and continue.py","a")
# a = f.write("Neeraj bhai bohot achha hai\n")
# print(a)
# f.close
#
# # Handle read and write both
f = open("Neeraj.txt", "r+")
print(f.read())
f.write("Here We Go")

# with open("Neeraj.txt") as f:
#     a = f.readline()
#     print(a)
# print(f.readline())
#
# f.close()