# MEMBERSHIP OPERATORS:-

str1 = "jbcsiegy2y99z8hxsrttr7wrx iruugr uyxwrgawxrwge xgseexgr EIeu@$$RYCRRCERUG IU$^&*((*))"

# check if str1 has @
# print("@" in str1)
# print("." in str1)
# print("G" in str1)
# print(str1.index('@'))
# print(str1.find('@'))
# print('@' not in str1)

list1 = ["Gamma", 23, 8, '8', '17', '@', 'Python', True, '0']

# print('a' in list1)
# print(17 in list1)
# print(0 in list1)
print("Python" in list1)

# check if "mm" is a member of any member of list1
# print("mm" in list1[0])


tup1 = (1, 2, 3, 4, 5, 6)
# print(tup1[6] in tup1)   #IndexError: tuple index out of range
# print(tup1[0] + tup1[1] in tup1[2])  #TypeError: argument of type 'int' is not iterable
# print(tup1[0] - tup1[1] not in tup1)

# set1 = {'Hello', 23, 9, False, '&', True, 8}
# # print(set1[2] - set1[5] in set1)  #TypeError: 'set' object is not subscriptable
# print('hello'.capitalize() in set1)
# print(0 in set1)


# set2 = {[1, 2, 3], ('A', 'B'), 'Yo', 45}  #TypeError: unhashable type: 'list'
# print([1, 2, 3] in set2)


# set3 = {'Calci', frozenset([12, 2, 3, 3, 4]), {1, 2, 3}, False}   #TypeError: unhashable type: 'set'
# print(0 in set3)


