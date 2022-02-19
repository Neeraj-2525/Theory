# part 1 - Calculate the factorial of a given number
# Part 2 - Find the number of trailing zeroes in that factorial
#
# def factorial(n):
#     product = 1
#     for i in range(1,n+1):
#         product *= i
#         print("factorial of the given number is", product)
#
#     return product
#
# def main():
#     n = int(input("Enter the number: "))
#     factorial(n)
#
# main()

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def factorialTrailingZeroes(number):
    count = 0
    i = 5
    while number // i != 0:
        count += int(number / i)
        i += 5
        return count
    # fac = factorial(number)
    # print(fac)
    # count=0
    # while (fac%10 == 0):
    #     count = count+1
    #     fac = fac/10
    #     return count


if __name__ == '__main__':
    number = int(input("enter the number: \n"))
    # fac = factorial(number)
    # print(f"The factorial is {fac}")
    print(factorialTrailingZeroes(number))
