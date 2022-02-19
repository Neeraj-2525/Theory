# subjects = ['english', 'mathematics','hindi']
# # # print(subject[-1])
#
# # name1 = "Rohan"
# # name2 = name1
# # print(id(name1), id(name2))       # Have same id
# # name2 = "Aman"
# # print(id(name1),id(name2))          # Have different id
# t = subjects
# t[0] = 'cs'
# print(subjects, t)
"""."""


# """
# Marks1 = ["Hindi", 80]
# Marks2 = ["Maths", 90]        # not recommended
# Marks3 = ["cs", 100]
# """
#
#
student1 = [["Hindi", 80], ["Maths", 90]]                # Two dimensional string
print(student1[1][1])

# for marks in student1:
#     print(marks[0])

# def factorialsum(n):
#     Sum1 = 1
#     for i in range(1, n + 1):
#         lum = 1
#         if i % 2 == 0:
#             Sum1 = Sum1 + (1 / i)
#         elif i % 2 != 0:
#             for j in range(1, i + 1, 1):
#                 lum = lum * j
#             Sum1 = Sum1 - (1 / lum)
#     return Sum1
#
#
# def main():
#     a = int(input("Enter the number : "))
#     print(factorialsum(a))
#
#
# main()


# list1 = ['Red', 'Green']
# list2 = ['Blue']
# colors = list1 + list2
# print(colors)

# list1 = [10,20]
# temp = list1
# list1 += [29]
# print(temp)


# numbers = [10,15,20,25,29]
# count = 0
# for marks in numbers:
#     if marks >= 25:
#         count+=1
# print(count)