num1 = input("enter num1:")
num2 = input("enter num2:")
try:
    print("the sum of these two numbers is ",
      int(num1)+int(num2))
except ValueError:


    print("Enter valid numbers")