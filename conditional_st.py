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
