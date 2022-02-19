"""."""
"""PYRAMID"""
#
# n = int(input("enter the number of lines : "))
# numStars = 1
# numSpaces = n-1
# """
#     print the pattern of a pyramid
#                                        *
#                                       * *
#                                      * * *
#     """
# for i in range(1,n+1,1):
#     print(" "*numSpaces + "* "*numStars)
#     numSpaces -= 1
#     numStars +=1

"""PYRAMID"""

# def pattern(n):
#     s = n
#     for i in range(0, n+1, 1):
#         print(" " * s, end="")
#         print("* " * i, end="")
#         print()
#         s -= 1
#
#
# def main():
#     n = int(input("enter the no. of line of pattern: "))
#     assert n > 0
#     pattern(n)


# main()

# """Reverse PYRAMID"""
#
# n = int(input("enter the number of lines: "))
# numStars = n
# numSpaces = 1
# """
# print the pattern of a pyramid
#
#                                      * * *
#                                       * *
#                                        *
# """
# for i in range(n, 0, -1):
#     print(" " * numSpaces + "* " * numStars)
#     numSpaces += 1
#     numStars -= 1

# """Reverse PYRAMID"""
# """
# print the pattern of a pyramid
#
#                                      * * *
#                                       * *
#                                        *
# """
# def pattern(n):
#     s = 0
#     for i in range(n, 0, -1):
#         print(" " * s, end="")
#         print("* " * i, end="")
#         print()
#         s += 1
#
#
# def main():
#     n = int(input("enter the no of line of pattern"))
#     assert n > 0
#     pattern(n)
#
#
# main()


# """
# To print the reverse right angled triangle
# """
# """
#                                    * * * * *
#                                    * * * *
#                                    * * *
#                                    * *
#                                    *
#
# """
# def pattern(n):
#
#     for numstars in range(n + 1, 0, -1):
#         print("* " * numstars, end="")
#         print()
#         numstars -= 1
#
# def main():
#     n = int(input("enter the no. of line of pattern: "))
#
#     pattern(n)
# main()
