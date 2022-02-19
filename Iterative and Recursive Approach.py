def factorial_iterative(n):
    """
    :param n: integer
    :return: n(n-1)(n-2)(n-3)....1
    """
    fac = 1
    for i in range(n):
        fac *= (i+1)
    return fac
#
#
# def factorial_recursive(n):
#     # """
#     # # :param n: integer
#     # # :return: n(n-1)(n-2)(n-3)....1
#     # # """
#     if n == 1:                              # When a function call itself
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
#
# number = int(input("enter your number: "))
# print(f"Factorial of {number} using iterative method: ", factorial_iterative(number))
# print(f"Factorial of {number} using recursive method: ", factorial_recursive(number))
#

# """Fibonacci Series"""
#
#
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# def main():
#     number = int(input("enter the number: "))
#     print(fib(number))
#
# if __name__ == '__main__':
#     main()
