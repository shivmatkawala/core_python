# CONTROL STATEMENTS:-

    # To perform same operation / action on multiple
    # elements we use control statements.
    # Control Statements do perform same action repeted.


# write a program wich greets.

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")


    # TYPES OF CONTROL STATEMSNTS:-
        # While loop
            # while loop give more control over program
            # than for loop.

            # while loop are manual in nature.
# count = 0

# while count < 5:      # header of while loop
#     print("Hello World")
#     count +=1


        # for loop

# for i in range(0, 5):
#     print("Hello world")


#----------------------------------------------

# print "Bye Bye World..!"  
# 10 times with the help of while loop

#-----------------------------------------------

# list_of_nums = [1, 2, 3, 4, 5]

# print square of list_of_nums numbers 
# using while loop.

# count = 0

# while count < len(list_of_nums):
#     print(list_of_nums[count] ** 2)
#     count +=1


#----------------------------------------------

# str1 = "HARIKANEHA"
#  print all the vowels from str1 
# use while loop


# index = 0
# while index < len(str1):
#     if str1[index] in "AEIOU":
#         print(str1[index])
#     else:
#         pass
#     index +=1


# write a program using while loop which will print
# table of 2.

# count = 1
# while count < 11:
#     print(2 * count)
#     count +=1


#---------------------------------
# tup1 = (1, 4, 2, 9, 6, 5, 8, 10, 22, 25)
# print only odd numbers from tup1

# index = 0

# while index < len(tup1):
#     if tup1[index] % 2 == 0:
#         pass
#     else:
#         print(tup1[index])

#     index +=1
    

# Q1)  find all capital letters from bellow lists strings

# list1 = ['AminI',  'aehMad', 'SravanThi', 'apple']
# count = 0
# while count < len(list1):
#     for i in list1[count]:
#         if i.isupper():
#             print(i)
#         else:
#             pass
#     count +=1


# find all the numbers from bellow string
# str2 = "dnduJBJBEWE872E 28E@#$O2S JASXIAEDUA)(*&^3 NUNITIUE2352"

# count = 0
# while count < len(str2):
#     if str2[count].isnumeric():
#         print(str2[count])
#     else:
#         pass
#     count +=1


# find duplicates and create there list from str3
# str3 = "ggUUstmmLqyeQxg"  # gUm

# duplicates = []

# for i in str3:
#     if str3.count(i) > 1:
#         if i not in duplicates:
#             duplicates.append(i)
#         else:
#             pass

# print(duplicates)

# index = 0

# while index < len(str3):
#     if str3.count(str3[index]) > 1:
#         if str3[index] not in duplicates:
#             duplicates.append(str3[index])
#         else:
#             pass
#     else:
#         pass
#     index +=1

# print(duplicates)

#--------------------------------------------------------


# print 1 to 5 numbers using while loop and using for loop

# count = 1
# while count < 6:
#     print(count, end=" <-> ")
#     count +=1

# for i in range(1, 6):
#     print(i)



# print all the small alphabets using while loop:

# count = 97

# while count < 123:
#     print(chr(count), end=" ")
#     count +=1


# print all those numbers which are 
# divisible by 5 in between 1 to 100:

# count = 1

# while count < 101:
#     if count % 5 == 0:
#         print(count)
#     else:
#         pass
#     count +=1


# find all the numbers which are divisible 
# 7 and 3 in between 1 and 100:


# from 11 to 99 print those numbers whose addition is less than 10

# Nested Loop

# list1 = [[1, 2], [3, 4], [5, 6]]
# # print only numbers from list1 

# for i in list1:
#     for j in i:
#         print(j)


# print("------------------------")

# for i in range(0, len(list1)):
#     for j in list1[i]:
#         print(j)




#----------------------------------------------------


# tup1 = (((1, 2, 3), (4, 5, 6)), ((7, 8, 9), (10, 11, 12)))

# for i in tup1:
#     for j in i:
#         for k in j:
#             print(k, end=" ")



# list2 = ["AMIN", "SALIM", "NADIM", "KHALIL", "JALIL"]
# # print only consonents from list2 

# unique_consonents = ""
# for i in list2:
#     for j in i:
#         if j not in "AEIOU":
#             if j not in unique_consonents:
#                 unique_consonents += j
#         else:
#             pass

# print(unique_consonents)

#--------------------------------------------------------------

# str1 = "ASDF$^&467bnm9as87654"
# # from str1 get all numbers and print them in ascending order 

# list1 = []
# for i in str1:
#     if i.isdigit():
#         if int(i) not in list1:
#             list1.append(int(i))


# list1.sort()
# print(list1)


# ask all family members ages and print there ages with there adjectives
# list_ages = []
# for i in range(4):
#     age = input("Enter age: ")
#     list_ages.append(age)



# list_ages.sort(reverse=True)
# members = ["Father", "Mother", "Brother", "Siter"]
# for j in range(len(list_ages)):
#     print(f"{members[j]} is {list_ages[j]} years old")



# ask user to enter his/ her inter second year subject wise marks:
    # physics
    # chemistry
    # maths 
    # biology

# you  will find the second highest marks
# subjcts = ["Physics", "Chemistry", "Maths", "Bioloy"]
# m = []
# for i in range(len(subjcts)):
#     marks = eval(input(f"Enter {subjcts[i]} marks:"))
#     m.append(marks)

# dict_marks = dict(zip(subjcts, m))

# for j in dict_marks.values():
#     print(j)



######################################

# find all the prime numbers from 10 to 100.

# for i in range(10, 100):
#     isPrime = True
#     for j in range(2, (i//2)+1):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         print(i)
#     else:
#         pass

#-------------------------------------

# print a fibonacci series ask user how many 
# numbers of fibonacci series to print.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# num_of_nums = int(input("How many fibonacci numbers you want: "))
# start = 0
# end = 1

# print(start)
# print(end)

# for i in range(0, num_of_nums-2):
#     start , end = end, start+end
#     print(end)

# =================

# ask user to enter an integer 
# and print its factorial.

# 5 --> 120
# 3 --> 6
# # 7 --> 5040
# num = int(input("Enter a number: "))
# factorial =  1
# for i in range(1, num+1):
#     factorial *= i 
# print(factorial)
#--------------------------------

# 75466724  --> sum of even nums, sum of odd nums

num = input("Enter only integer with min 5 digits: ")

sum_even = 0
sum_odd = 0

for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        sum_even += int(num[i])
    else:
        sum_odd += int(num[i])

print(f"SUM OF EVENS: {sum_even}, SUM OF ODDS: {sum_odd}")

