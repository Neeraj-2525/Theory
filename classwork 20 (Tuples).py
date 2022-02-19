t = [10, 20, 30, 40, 20,34,54,64]
# print(t, id(t))
# t.append([50, 98])                   # append only takes a single element at a time
# print(t, id(t))


# print(t, id(t))
# t.extend([50, 69])                   # extend takes sequence of elements (and single element)
# print(t, id(t))

# v = t.pop(2)                         # Remove the element from the given index
# print(v, t)


# unwanted_num = {20}
# t = [ele for ele in t if ele not in unwanted_num]
# print(t)
"""OR"""
# num = 20
# while num in t:                         # To remove multiple elements at a time
#     t.remove(20)
# print(t)

names = ['Ram', 'Shyam', 'Kam', "Joy"]
# rollNUms = [1,2,3,4]
# indexOfShyam = names.index('Shyam')
# names.remove('Shyam')
# rollNUms.pop(indexOfShyam)
# print(names, rollNUms)


# del t[2:6]
# print(t)                    # Delete the elements from the list

# del t                         # Delete whole list and variable name also
# print(t)

# names.insert(5, 'Shyam')       # insert object before given index
# print(names)

# names.reverse()
# print(names)

# t.sort()                        # ascending order
# print(t)

# t.sort(reverse= True)            # descending order
# print(t)

# names.sort(key=len)                 # sorting over length
# print(names)


#cubes of number in range 1 to 10
# cubes = []
# end = 10
# for i in range(1, end+1):
#     cubes.append(i**3)
# print(cubes)

# List comprehension
# cubes = [i**3 for i in range(1,10+1)]
# print(cubes)

# multiplication table of 5
# res = []
# for i in range(1,10+1):
#     res.append(5*i)
# print(res)
"""OR"""
# res = [i*5  for i in range(1,10+1)]
# print(res)


# res = []
# for i in range(1,4):
#     for j in range(1,4):
#         res.append([i,j])
# print(res)
"""OR"""
res = [ (i,j)  for i in range(1,4) for j in range(1,4)]
print(res)

m = [i for i in range(1,11)  if i%3==0 ]        # Multiples of 3
print(m)

