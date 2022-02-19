# def duplicate(old_list):
#     final_lst = []
#     [final_lst.append(num) for num in old_list if num not in final_lst]
#     return final_lst
#
# if __name__ == '__main__':
#     duplst = eval(input("enter the list: "))
#     print(duplicate(duplst))

"""----------------------------------------------------------------"""
"""Dictionary"""
#       Key:Value | key should be unique, value can be mutable
# months = {1: 'Jan', 2: 'Feb', 3: 'March'}
# print(months[1])
# for i in months:
#     print(i, months[i])

# temp = {('raman', 'sahil'):1, 'sahil':2}
# print(temp)
# """as dictionaries are immutable so they
# don't support lists as key and supports tuples"""

# month = {0:'NoMonth'}
# month[2] = 'February'
# month[1] = 'January'
# print(month)

# Operations
digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(digits[1])
print(len(digits))
print(max(digits))
print(min(digits))  # Operations can only be applied on key not on value
print(sum(digits))
print(5 in digits)
del digits[1]
print(digits)
print(digits.clear)  # Delete the complete dictionary!
print(digits.get(3))
print(digits.get(6))  # Don't give error rather indexing gives
print(digits.get(6,'six'))
digits.get(6,'six')
print(digits[6])