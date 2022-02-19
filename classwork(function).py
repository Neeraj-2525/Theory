def function1(a,b):
    print("Hello you are in fun function1:",a+b)


def function2(a,b):
    """this is a function which calculate average of two numbers
     this function doesnt work for three numbers"""
    avg = (a + b) / 2
    return avg

v=function2(5,7)
print(function2.__doc__)