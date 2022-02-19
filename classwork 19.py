# def isPalindrome(s):
#     return s == s[::-1]
#
#
# s = input("Enter your string here: ")
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")

# HW count the number of common characters in a pair of str refer to 6.2.2 from book

# fruit = {'cherry', 'apple'}
# fruit.update(('grapes', 'banana'))
# fruit.remove('apple')
# fruit.clear()
# print(fruit)

aset = {11,22,33}
bset = {12,23,33}
# c = aset.union(bset)
c = aset.intersection(bset)
print(c)