#Name: NEERAJ KUMAR
#Roll No. : 21/73038

"""
Objective: To compute the multiplicative table for the number given as a input from the user.
"""

def main():

    number = int(input("enter the number:"))

    for count in range(1,11):
        print(number,'x',count,'=',number*count)

main()