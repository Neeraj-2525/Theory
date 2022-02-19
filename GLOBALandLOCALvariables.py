# l = 10            # Global varianle
# def func1(n):
#     l = 5         # Local variable
#     m = 8         # Local variable
#     global l      # To get permission to change global variable
#     l += 45       # Value of a Global Variable can't be changed
#     print(n, "I have printed")
#     print(l, m)
# func1("This is me")
# print(l)
# # print(m)        # Show error as m is not defined

def neeraj():
    x = 20
    def n33raj():
        global x
        x = 88
    print("before calling n33raj()", x)
    n33raj()
    print("after calling n33raj()", x)
