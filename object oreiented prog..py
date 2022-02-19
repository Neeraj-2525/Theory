# Classes - Template
# Object - Instance of the Class
# DRY - Do not repeat yourself
# get_no_of_films(table)
"""==="""
# class Student:
#     pass
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.subjects = ['hindi', 'chemistry']
# print(harry.name, harry.std, harry.section, larry.subjects)
# # print(harry, larry)    dono alag hai
'''==='''
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
# harry = Employee("Harry", 455, "Instructor")                                       # oops 2,3
# rohan = Employee("Rohan", 255, "Student")
#
# # harry.name = "Harry"
# # harry.salary = 455
# # harry.role = "Instructor"
# #
# # rohan.name = "Rohan"
# # rohan.salary = 4554
# # rohan.role = "Student"
# print(harry.printdetails())
# # print(rohan.printdetails())
# # print(Employee.__dict__)
# # Employee.no_of_leaves = 9           # change isse hi hoga!
# # print(harry.no_of_leaves)
"""==="""
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves = newleaves
#
#
# harry = Employee("Harry", 455, "Instructor")                                       # oops 4
# rohan = Employee("Rohan", 255, "Student")
# harry.change_leaves(34)
# print(harry.no_of_leaves)
"""==="""
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         # params = string.split("-")
#         # return cls(params[0], params[1], params[2])
#         return cls(*string.split("-"))                  # one liner uper wale ka
#
# harry = Employee("Harry", 455, "Instructor")                                       # oops 5
# rohan = Employee("Rohan", 255, "Student")
# karan = Employee.from_str("Karan-322-Student")
# print(karan.salary)
"""==="""


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


harry = Employee("Harry", 455, "Instructor")  # oops 5
rohan = Employee("Rohan", 255, "Student")
print(harry.printdetails())
