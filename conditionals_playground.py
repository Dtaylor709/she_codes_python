# #boolean

# HAYLEYS COURSE EXEMPLES

# is_raining = True
# is_cold = True
# # print(type(is_raining))
# # print(type(is_cold))

# # print(is_raining) #True
# # print(not is_raining)#False
# # print(is_raining or is_cold) #True
# # print(is_raining and not is_cold)#False
# # print(is_raining or not is_cold)#True becaue if there is and 'or' if there is any True in the sentence it will default to true
# # print(not is_raining and not is_cold)#False

# # print()
# # temp = 16
# # print(temp < 18)
# # print(temp > 18)

# # # a double == equal sign is used to compare two strings with each other as the same
# # # != it compare two things as 'not' the same

# # code = "freeticket"
# # print(code == "freeticket")
# # print(code != "freeticket")

# is_raining = True
# if is_raining:
#     print("Take an umbrella")
# else:
#     print("Do not take an umbrella")
# print("cats")    

# # 'else' must always follow an if statement. you cannot hve else by itself. instead you can use 'if not [value]'
# # 'elif' = elseif so if the first if isn't true then the program checks the next statement which would be an elif. There is no limit to the number of elif you can have

# temp = 16
# wind_chill = 4

# if temp - wind_chill <16:
#     print("Take a jumber")
# elif temp - wind_chill > 30:
#     print("It is hot, Stay home.")
# else:
#     print("Wow, what a lovely day")

# # you can have If inside each other. There is no limit but good practice is to only repat IF 3 times.

# if temp < 16:
#     if is_raining:
#         print("just stay home")
#     else:
#         print("It's okay today")
# else:
#     print()



#CONDITIONALS EXERCISES
# 
# QUESTION 1 

# moths_in_house = True

# if moths_in_house:
#     print("Get the moths")
# else:
#     print("No threats detected")

# QUESTION 2

# moths_in_house = False
# mitch_is_home = True

# if moths_in_house:
#     if mitch_is_home:
#         print("Hoooman! Help me get the moths")
#     else:
#        print("Meooooooooooooow! Hissssss!")
# else:
#     if mitch_is_home:
#         print("Climb on Mitch.")

#     else:
#         print("No threats detected")
    
# QUESTION 3 

# light_colour = "Red"
# car_detected = True

# if light_colour == "Red":
#     if car_detected:
#         print("Flash!")
# else:
#     print("Do nothing.")

# QUESTION 4 

# height = int(input("what is your height (cm)")) you can put the int on th input line if you hve more than one if statement

# if height > 120:
#     print("Hop on!")
# else:
#     print("Sorry, not today :( ")

# # QUESTION 5 

# name = input("Enter your username: ")
# password = input("Enter your password: ")

# if name == "Fleur"and password == "password123":
#         print("Correct!")
# else:
#     print("Incorrect!")

# Question 6 

email = input("Enter your email address: ")

if email == "hayley@test.com" or email == "hayley.test@com":
        print("Valid email address.")
else:
    print("Invalid email address.")