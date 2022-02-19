"""classwork14"""
"""
1.sum of first n natural numbers
2.factorial n, n! = 1x2x3x4x5
3.squares of n natural numbers
"""

# def main1():
#     sum = 0
#     n = int(input("Enter the number to get the sum of first natural numbers: "))
#     for i in range(1, n + 1):
#         sum += i
#     print(sum)
#
# main1()


# def main2():
#     product = 1
#     n = int(input("Enter the number to get the factorial: "))
#     for i in range(1, n + 1):
#         product *= i
#     print(product)
#
# main2()

#series of squares of first natural numbers
# n = int(input())
# for i in range(1, n+1):
#     i = i**2
#     print(i)

#print the following: -1,4,-9,16,...
# n = int(input())
# for i in range(1,n+1):
#     print(((-1)**i)*i*i)


"""FIBONACCI SERIES"""
"""first=0
second=1
third=first+second              0,1,1,2,3,5,8...
print(third)"""

"""
1. approach
"""
#Generate first n terms of fibonacci series
n=7
first = 0
second = 1
third = first + second
print(first, second, third, end=" ")
for i in range(1,n-2,1):      #as 3 out of 7 terms are printed so n-3=4
    first = second
    second = third            #Output: 0,1,1,2,3
    third = first + second
    print(third, end=" ")

"""
2. approach
"""
#Generate first n terms of fibonacci series
# def Fib(n):
#
#     first = 0
#     second = 1
#     if n == 1:
#         print(first)
#     elif n == 2:
#         print(first, second)
#     else:
#         third = first + second
#         print(first, second, third, end=" ")
#         i = 0
#         while i < (n-3):
#             first = second
#             second = third
#             third = first+second
#             print(third, end=" ")
#             i += 1
# def main():
#     n = int(input("Enter the number of times you want to print: "))
#     Fib(n)
#
# main()
