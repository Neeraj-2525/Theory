# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num*fact(num - 1)
#
# def main():
#     num = int(input("enter number: "))
#     print(fact(num))
#
# if __name__ == '__main__':
#     main()

# def fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fib(num - 1) + fib(num - 2)
#
# def main():
#     num = int(input("enter the number: "))
#     print(fib(num))
#
# if __name__ == '__main__':
#     main()

# def sum(num):
#     if num == 0:
#         return 0
#     else:
#         return sum(num-1) + num
#
# def main():
#     num = int(input("enter the num: "))
#     print(sum(num))
#
# main()

# LINEAR SEARCH
# lst = [1, 2, 3, 4, 5, 6, 7]
# # for i in range(0, len(lst)):
# #     if i == 5:
# #         print(lst[i])
#
# def linearsearch(l, val):
#     for i in range(0,len(l)):
#         if l[i] == val:
#             # print(i)
#             return i
#
#
# def main():
#     l = eval(input("enter the list: "))
#     val = int(input("enter the element: "))
#     index = linearsearch(l, val)
#     print("val found at index", index)
#
# main()

"""
----------------------------------------
        Binary Search Algorithm
----------------------------------------
"""
# iterative implementation of binary search in Python
print(__doc__)
pos = -1


def bnry_search(lst, n):
    l = 0  # Lower bound of list (first index)
    u = len(lst) - 1  # Upper bound of list (last index)

    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid - 1


lst = eval(input("enter your list: "))
lst.sort()
n = int(input("enter the element to be found: "))

if bnry_search(lst, n):
    print("Found at", pos + 1)
else:
    print("Not Found")

# recursive implementation of binary search in Python
# def binary_search_recursive(a_list, item):
#     """Performs recursive binary search of an integer in a given, sorted, list.
#     a_list -- sorted list of integers
#     item -- integer you are searching for the position of
#     """
#     first = 0
#     last = len(a_list) - 1
#     if len(a_list) == 0:
#         return ' was not found in the list'.format(item=item)
#     else:
#         i = (first + last) // 2
#         if item == a_list[i]:
#             return ' found'.format(item=item)
#         else:
#             if a_list[i] < item:
#                 return binary_search_recursive(a_list[i+1:], item)
#             else:
#                 return binary_search_recursive(a_list[:i], item)
