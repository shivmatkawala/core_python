# CONDITIONAL STATEMENTS:-
    # this is the technique in any programming language 
    # which returns answer / output on the basis of condition.

# EXAMPLE:-
    # Program is asking you to enter marks,
    # Program will assign / return grade on the basis of marks.



# KEY WORD IN CONDITIONAL STATEMENTS:-
    # if

# marks = int(input("Enter marks: "))

# if marks < 40:
#     print("Fail")

# if marks >= 40 and marks < 60:
#     print("Second class")

# if marks >= 60 and marks < 80:
#     print("First class")

# if marks >= 80 and marks < 101:
#     print("Distinction")



# gender = input("Enter your gender: ") # Male, Female

# if gender == "Male":
#     print("You can marry at age of 22.")

# if gender == "Female":
#     print("You can marry at age of 18.")


# gender = input("Enter your gender: ")

# if gender == "Male":
#     print("You can marry at 50")

# elif gender == "Female":
#     print("You can marry at 100")


# gender = input("Enter your gender: ")

# if gender == "Male":
#     print("You can marry at 50")

# elif gender == "Female":
#     print("You can marry at 100")

# else:
#     print(f"there is no such gender called '{gender}'")


#-----------------------------------------------------

# Write a program  which asks user to enter there 
# indian states capital city and print the state.

# capital = input("Enter your capital city: ")

# if capital == "Mumbai":
#     print("Maharashtra")
# elif capital == "Hyderabad":
#     print("Telangana")
# elif capital == "Chennai":
#     print("Tamilnadu")
# elif capital == "Banglore":
#     print("Karnataka")
# elif capital == "Vaizag":
#     print("Andhra")

# else:
#     print(f"Sorry, i have no information about {capital} in database.")

dict_of_state_capitals = {
    "Banglore": "Karnataka",
    "Hyderabad": "Telangana",
    "Mumbai": "Maharashtra",
    "Amdawad": "Gujrat",
    "Jaipur": "Rajsthan"
    }

# capital = input("Enter your capital city: ")

# if capital in dict_of_state_capitals.keys():
#     print(dict_of_state_capitals[capital])
# else:
#     print(f"Sorry, i have no information about {capital} in database.")


# ------------------------------------

# write a program where you ask user to enter 
# a numer.check if number is even or odd and print.

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")

# else:
#     print("Odd")


#----------------------------------------------------

# IF  ---> only one time and for first condition it can be used
# ELIF --> multiple times and except for first condition it can be used
# ELSE --> only one time and last condition it can be defined

# thief and police:-
    # thief --> lost
    # police --> won

# role = input("what do you want to be: ")

# if role == "police":    # condition1
#     print("Won")
# else:                   
#     print("Lost")


# Ask user to enter the name:-
    # check if name has at least 5 charecter.
    # if exact 5 charecters --> print ("Good Name")
    # if less then 5 charecters --> print("short name")
    # if more than 5 charecters --> print("Big name")
    # if user didnt enter any name ---> print("Dont you have a name ?")

# username = input("Enter your name: ")

# if len(username) == 5:
#     print("Best name")

# elif len(username) > 5:
#     print("Big name")

# elif len(username) < 5 and len(username) > 0:
#     print("Small name")

# else:
#     print("Dont you have a name ?")


#------------------------------------------------------

# ask  user  to enter a number 
    # check if number is positive or negative or zero
        # if positive print (entered positive number.)
        # if negative prinnt(entered negative number.)
        # if 0 print(enetered 0)

# num = int(input("Enter a number: "))

# if num == 0:
#     print("You have entered 0")
# elif num > 0:
#     print("You have entered positive number")
# elif num < 0:
#     print("you have entered ngative number.")
# else:
#     print("You entered nothing.")


# ask user to enter a string
    # if string is a palindrome 
        # print Palindrome
    # if string is not a palindrome
        # print No palindrome
    
# BOB  --> BOB
# MADAM --> MADAM
# 12321 --> 12321

# str1 = input("Enter a string: ")

# if str1 == str1[::-1]:
#     print("Palindrome")

# else:
#     print("No Palindrome")



l1 = [12, 34, 56 ,78 ,90, 45]

# write a program which will aanalyze l1 list
# if the difference between the biggest number of l1 
# and smallest number of l1 is greater than 50 --> "huge difference"
# if difference is less than 50 or equal to 50 then say "small difference"