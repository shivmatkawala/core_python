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

str1 = "HARIKANEHA"
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
tup1 = (1, 4, 2, 9, 6, 5, 8, 10, 22, 25)
# print only odd numbers from tup1

index = 0

while index < len(tup1):
    if tup1[index] % 2 == 0:
        pass
    else:
        print(tup1[index])

    index +=1
    