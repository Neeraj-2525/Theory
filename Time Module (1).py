import time

initial = time.time()
k = 0
while (k<45):
    print("This is Neeraj")
    time.sleep(2)                                               # Ruk kar play karta hai
    k+=1
print("while loop ran in", time.time() - initial, "seconds")
                                                                # To find time for loop runs
# initial2 = time.time()
# for i in range(45):
#     print("This is Neeraj")
# print("for loop ran in", time.time() - initial2, "seconds")
#
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)