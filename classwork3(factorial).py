product = 1
n= int(input("enter the value of n : "))

assert n>=0

for i in range(1,n+1):


    product = product * i
    
    print("factorial of",n, "is : ", product)


