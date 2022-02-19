# # Print multiplication table for n numbers
# n = int(input("Enter the number: "))
# for j in range(0,n):
#     print("\nMultiplication table of", n)
#     for i in range(1,11):
#         print(n,"x",i,"= ",n*i)


# #Nested for loop
# N = 3
# total = 0
# for i in range(1,N+1):
#     print("Inner for loop")
#     for j in range(i,N):
#         print(i,j)
#         total += i+j
# print(total)


#Pattern question
"""."""
"""
                           1
                          121
                         12321
                        1234321

"""
"""
1
2
3
4
i  this is varying
                    for i = 4
                    #1to4
                    #4to1

"""
# num = 4
# spaces = num - 1
# for i in range(1,5):
#     print(" "*spaces, end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     spaces -=1
#     print()


''' :-)'''
"""WHILE LOOP"""
#
# count=5
# while count >= 1:                    # count till 5
#     print(count)
#     count-=1
# print("end")

# total, n = 0, 5
# for count in range(1,n+1):            # sum of first 5 natural numbers by using for loop
#     total += count
#     print(total)

# total, n = 0, 5
# count = 1
# while count<=n:                        # sum of first 5 natural numbers by using while loop
#     total+=count
#     count+=1
# print(total)


# total = 0
# num = input("enter a number: ")
# while num != "":
#     total += int(num)                    # print total till user providing input
#     num = input("enter a number: ")
# print("sum of all input numbers is", total)
#
#
# def main():
#     total = 0
#     num = int(input("enter the number: "))                    # Sum total of digits
#     total = sumOfDigits(num)
#
#
#
num = int(input("enter the number: "))
total = 0
while(num!= 0):                                                 # Sum total of digits 2
    digit = num%10
    total += digit
    num = num//10
print(total)


