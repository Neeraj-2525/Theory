# numbers = ["3", "43", "64"]
# numbers = list(map(int, numbers))
# numbers[2] = numbers[2]+1
#
# num = [2,3,4,5,6,7,8]
# square = list(map(lambda x: x*x, num))
# print(square)
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2]+1
# print(numbers[2])

"""MAP FUNCTION"""
def square(a):
    return a*a
def cube(b):
    return b**3                                # square and cubes
func = [square, cube]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

"""FILTER FUNCTION"""
list1 = [3,4,5,6,7,3,9,88]
def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list1))
print(gr_than_5)

"""REDUCE"""
from functools import reduce

list1 = [2,3,4,5,6,7,8]
num = reduce(lambda x,y:x+y, list1)
print(num)