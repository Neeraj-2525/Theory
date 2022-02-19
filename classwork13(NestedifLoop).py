def maximum3(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            maxNumber = n1
        else:
            maxNumber = n3
    elif n2 > n3:
        maxNumber = n2
    else:
        maxNumber = n3
    return maxNumber


def main():
    n1 = int(input("enter the first number: "))
    n2 = int(input("enter the second number: "))
    n3 = int(input("enter the third number: "))
    maximum = maximum3(n1, n2, n3)
    print("Maximum Number is", maximum)


main()
