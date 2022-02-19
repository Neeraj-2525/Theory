# passwords = {"raman":"@@@@", "kishor":"$$$$"}
# morePasswords = {}
# morePasswords["rahul"] = "secret"
# # print(passwords)
# passwords.update(morePasswords)     # add more key value pairs
# # print(passwords.keys())

# months = {1:'Jan', 2:'Feb', 3:'Mar'}
# for index in months.keys():
#     print(months[index])      # to print keys
# print(max(months))            # max applied only on key part
# print(months.items())         # return a tuple of key values
# print(months.get(1))          # returns the value associated with that key
# print(months[2])              # same

# def compute_cube():
#     cubes = {}
#     for i in range(1, 6):
#         cubes[i] = i ** 3
#     print(cubes)
#
#
# def main():
#     compute_cube()
#
#
# main()

# Q14
# cubes = {i:i**3 for i in range(1,6)}        # shortcut
# print(cubes)

# Q13
# def countVowel():
#     content = input("enter your string here: ")
#     # f.read() to read the content
#
#     vowelsCount = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#
#     vowels = vowelsCount.keys()
#     for char in content.lower():
#         if char in vowels:
#             vowelsCount[char] += 1
#
#     print(vowelsCount)
#
#
# countVowel()

# Q13 Alternative
# def char_count():
#     f = open("Neeraj.txt", "rt")
#     content = f.read()
#     characters = {}
#     data = content.lower()
#     for char in data:
#         if char not in characters.keys():
#             characters[char] = 1
#
#         else:
#             characters[char] += 1
#
#     print(characters)
#     f.close()
# char_count()

# to count the characters in a string
# def countChars():
#     content = "pythOn is a progrAmming lAnguagE"
#     charCount = {}
#     data = content.lower()
#     for char in data:
#         if char not in charCount.keys():
#             charCount[char] = 1
#         else:
#             charCount[char] += 1
#     print(charCount)
#
#
# countChars()