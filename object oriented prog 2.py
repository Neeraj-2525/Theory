"""==="""


"""single inheritence"""

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         # params = string.split("-")
#         # return cls(params[0], params[1], params[2])
#         return cls(*string.split("-"))  # one liner uper wale ka

# class Programmer(Employee):
#     def __init__(self, aname, asalary, arole, language):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.language = language
#
#
#     def printprog(self):
#         return f"The programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}. The languages are {self.language}"
#
#
# harry = Employee("Harry", 455, "Instructor")  # oops 5
# rohan = Employee("Rohan", 255, "Student")
#
# shubham = Programmer("Shubaham", 555, "Programmer", ["python"])
# karan = Programmer("Karan", 777, "Programmer", ["python", "cpp"])
# print(karan.printprog())


"""MULTIPLE INHERITENCE"""

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))  # one liner uper wale ka

class Player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. Game is {self.game}"

class CoolProgrammer(Employee, Player):
    language = "C++"

    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 455, "Instructor")  # oops 5
rohan = Employee("Rohan", 255, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", 9999, "coolprogrammer")
det = karan.printlanguage()
# print(det)