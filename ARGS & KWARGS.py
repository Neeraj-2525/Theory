def funargs(normal, *args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    print("Now I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is {value}")
# Nee = ["Neeraj", "Rohan", "Shivam", "Harry"]
Nee = ["Neeraj", "Rohan", "Shivam", "Harry"]
normal = "I am a normal argument and the students are:"
kw = {"Neeraj":"programmer", "Rohan":"Monitor", "Shivam":"Instructor", "Harry":"Teacher"}

funargs(normal, *Nee, **kw)
