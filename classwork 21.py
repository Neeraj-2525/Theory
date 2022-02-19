"""classwork 21"""

# def listupdate(lst, index, value):
#     lst[index] = value
#     print(lst)
#
#
# def main():
#     lst = [10,20,30,[40,50]]
#     listupdate(lst,1,15)
#     print(lst)
#
#
# main()

# import copy
# lst1 = [10,20,[30,40]]
# lst2 = copy.copy(lst1)
# #for index in range(len(lst2)):     # Copying a list and modifying without changing orig.
# lst2[2][0] += 5                     # copy.copy: prblm .. changing the orig.list also in 2d list
# print(lst1,lst2)

# lst1 = [10,20,[30,40]]
# lst2 = copy.deepcopy(lst1)
# #for index in range(len(lst2)):     # Copying a list and modifying without changing orig.
# lst2[2][0] += 5                     # so we use .deepcopy
# print(lst1,lst2)

"""TUPLES"""
# weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat")
# # Tuples are immutable
# myTuple = (8, 3, 'apple', {3, 4, 5})

# l1 = ("one")
# print(l1,type(l1))      # type = str not tuple
# newTuple = (str(i) for i in range(6))
# print(newTuple)

# colors = ('red', 'yellow', 'orange')
# fruits = ('cherry', 'banana', 'orange')
# fruitColor = list(zip(colors,fruits))
# print(fruitColor)

# a='1234'
# val = [23,43,54]
# print(list(zip(a,val))) # will print 3 touples

# built-in function in tuples
def inc(a,b):
    a += 2
    b += 2
    return a,b
def main():
    a,b = 10,20
    a,b = inc(a,b)
    print(a,b)
main()
