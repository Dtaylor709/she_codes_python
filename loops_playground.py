# HAYLEYS LOOP COURSE EXAMPLES

# num = number. You can actualy use any word you wnat 
# use range() instead of [0:10]. range =up to number so range (10) only prints 0 to 9 as it prints 10 items but te list starts with 0
# # for loop starts with 'for'

# for num in range(10):
#     print(num)

# # (1, 11) means start at position 1 and go up to 11 items. It will list 0 to 10 but because we said start at 1
# for num in range(1, 11):
#     print(num)

# # fist number what item to start list with. 
# # second number what number to go up to
# # third number what increment to go up numbers with. 2 is every second number
# for num in range(0, 11, 2):
#     print(num)

# # use a for loop to print numbers 0 to 100 (inclusive)
# for index in range(101)
# print(index)

# # # use a for loop to print numbers
# # 0 to 100 in steps of 5 (5, 10)

# for chocolate in range (0, 101, 5)
# print(chocolate)


# # you can put text next to each item in a list by doing the below

# chilli_wishlist = [
#  "igloo",
#  "chicken",
#  "donut toy",
#  "cardboard box" 
# ]

# for item in chilli_wishlist:
#     print(f"Chilli wants: {item}")

# WHILE LOOPS

# != exlamation mark= means not equal to

# guess = ""
# while guess != "a":
# #     guess = input("Guess a letter")

# counter = 0
# while counter <= 5:
#     print(counter)
# #     counter = counter + 1

# EXERCISE: FOR LOOPS

# QUESTION 1A

# number = input("Enter a number: ")
# for list in range (1,4):
#     answer = list * int(number) 
#     print(f"{number} * {list} = {answer}")

# # QUESTION 1B

# number = input("Enter a number: ")
# for list in range (1,8):
#     answer = list * int(number) 
#     print(f"{number} * {list} = {answer}")

# QUESTION 2

number = int(input("Enter a number: "))
sum = 0
upto = (1,n)
for item in range [1, int(number)]:
    answer = item + int(number)
    print(f"{answer}")

# Ask the user for a number. Use a for loop to sum from 0 to that number
# addition = int(input("Enter a number."))
# sum = 0
# for i in range(addition + 1):
#   sum = sum + i
#   i = i + 1
# print("Sum is ", sum)