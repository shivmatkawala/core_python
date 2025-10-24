# Ternary Operator

# x = 100

# # I want to print "Big" if number is bigger than 20
# # else print "Small"

# ans = "Big" if x > 20 else "Small"
# print(ans)


# color = "Yellow"

# ret = "Sacrifice" if color.title() == "Red" else "Nature"
# print(ret)



# age = eval(input("Enter your age: "))

# eligibility = "Eligible for Voting" if age >= 18 else "Not eligible for voting"
# print(eligibility)


# Ask student to enter marks

# if marks < 40 -->  fail
# if marks >= 40 and marks < 60  -- pass
# if marks >=60 and marks < 80 -- first class
# if marks >= 80 and marks < 100 --> distingtion 


# marks = eval(input("Enter marks: "))

# result = "Fail" if marks < 40 else "Pass" if marks >= 40 and marks <60 else "First Class" if marks >= 60 and marks < 80 else "Distingtion" if marks >=80 and marks <100 else "Incorrect Marks"
# print(result)


##############################################

# ASK USER HIS or HER NAME and COUNT
# ALL THE CONSONENTS in NAME.
# IF COUNT of CONSONENT > 5 --> 
    # GREAT NAME YOU have more than 5 CONSONENTS.
# IF COUNT of CONSONENTS < 5 ---> 
    # BEST NAME You have less  than 5 CONSONENTS.

# name = input("Enter your name: ")
# list_name = list(name
# vowels = "aeiou"
# for i in list_name:
#    if i in vowels:
#       list_name.remove(i)
# count_of_consonents = len(list_name)
# ans = "GREAT NAME YOU have more than 5 CONSONENTS." if count_of_consonents > 5 else "BEST NAME You have less  than 5 CONSONENTS."
# print(ans)


# ASK USER TO ENTER a favorate primary color
# if fav_color is Red --> Anger
# if fav_color is green --> nature
# if fav_color is blue --> peace

# fav_primary_color = input("Enter favourate primary color: ")
# output = "Anger" if fav_primary_color.title() == "Red" else "Nature" if fav_primary_color.title() == "Green" else "Peace" if fav_primary_color.title() == "Blue" else "Enter Only Primary Colors [Red, Green, Blue]"
# print(output)

# Ask User to enter a favorate number.
# if favorate number is integer and even 
    # print "You entered integer and even number"

# if favorate number is integer and odd
    # print "You entered integer and odd number"

# if favourate number is float
    # print "You entered float"

# if neither float nor int 
    # print "Please enter only int and float"


# fav_number = input("Enter a favourate number: ")
# ans = "You entered integer and even number" if type(eval(fav_number)) == int and int(fav_number) % 2 == 0 else "You entered integer and odd number" if type(eval(fav_number)) == int and int(fav_number) % 2 != 0 else "You entered float" if type(eval(fav_number)) == float else "Please enter only int and float"
# print(ans)

