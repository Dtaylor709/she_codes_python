# HAYLEYS COURSE EXAMPLES

# chilli_wishlist = [
#  "igloo",
#  "chicken",
#  "donut toy",
#  "cardboard box" 
# ]
# print(chilli_wishlist[0])

# # NUMBERING STARTS AT 0. IF YOU PUT NUMBER IN BRACKETS you can ask them to only print the item the number is. in this cse 0 is the frst item
# # print(len()) = length of list = it will show how many items are in the list

# print(len(chilli_wishlist))

# print(chilli_wishlist[-1])

# # if you put -1 it will show the last item in the list because 0 is the first item so -1 is the item before zero.
# print(chilli_wishlist[0:2])

# # if you use [0:2] is will show the item in the first and second position (0 and 1) but not the third item represented by 2.

# chilli_wishlist[1] = "carrot"
# print(chilli_wishlist)

#  you can substitute new items into the existing list by using = and stating the new item name

# print sublist of items in positions 2 through to 3. 
# as the list of 4 items starts at 0 positions 2 and 3 are 3 &4 on the list. To get position 3 you put 4 which doesn't exist in order to capture it
# print(chilli_wishlist[2:4])
# # print item in -3 position
# print(chilli_wishlist[-3])

# # .append will add one item to the end of the list. If you print the list again that item will show
# chilli_wishlist.append("dig mat")
# print(chilli_wishlist)


# # .extend will add more than one item in a list to another list.
# chilli_wishlist.extend(["kong","tennis ball", "crocodile toy"])
# print(chilli_wishlist)

# # .insert will add something in a specific position. state the position number followed by the text.
# chilli_wishlist.insert(1, "peanut butter")
# print(chilli_wishlist)

# # .pop = removes items
# # if you have .pop() with blank insode the brackets it will delete the last item on the list
# print(chilli_wishlist.pop())
# print(chilli_wishlist)
# # if you wan to remove an item at a specific position put the position number in the brackets
# print(chilli_wishlist(2))
# print(chilli_wishlist)
# # you can also remove a specific item by putting the name of the item in brackets
# chilli_wishlist.remove("kong")
# print(chilli_wishlist)


# chilli_wishlist = [
#  "igloo",
#  "chicken",
#  "donut toy",
#  "cardboard box" 
# ]

# # add a new item to position -2
# chilli_wishlist.insert(-2, "chocolate")
# print(chilli_wishlist)
# # remove the 3rd item from the list
# print(chilli_wishlist.pop(2))
# # addd four new items to the end of the list
# print(chilli_wishlist.extend(["cats", "horse", "panda", "dolphin"]))
# # remove "igloo" item from the list
# chilli_wishlist.remove("igloo")
# print(chilli_wishlist)


# chilli_wishlist = [
#     ["igloo"], # bed
#     ["donut toy", "tennis ball", "crocodile"], #toys
#     ["chicken", "peanut butter"], # treats
#     ["cardboard box", "kong"] # puzzles
# ]

# print(chilli_wishlist)
# print(chilli_wishlist[0][0])
# print(chilli_wishlist[3][0])

# # the first [] gets the position of the list. The second [] gets the position ytem within that list. e.g. [0][0] will show the first list and first item in that list

# LISTS EXERCISES

# QUESTION 1

# foods = [
#     "orange",
#     "apple",
#     "banana",
#     "strawberry",
#     "grape",
#     "blueberry",
#     ["carrot", "cauliflower", "pumpkin"],
#     "passionfruit",
#     "mango",
#     "kiwifruit"
# ]

# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print(foods[0:3])
# print(foods[-3:])
# print(foods[6][2])

# QUESTION 2

# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]


# print(f"{mailing_list[0][0]} : {mailing_list[0][1]}")

# print(f"{mailing_list[1][0]} : {mailing_list[1][1]}")

# print(f"{mailing_list[2][0]} : {mailing_list[2][1]}")

# print(f"{mailing_list[3][0]} : {mailing_list[3][1]}")

# print(f"{mailing_list[4][0]} : {mailing_list[4][1]}")


# QUESTION 3

# names_list = []

# name = input("what is your name? ")
# name2 = input("what is your name? ")
# name3 = input("what is your name? ")

# names_list.append(name)
# names_list.append(name2)
# names_list.append(name3)

# print(names_list)

#SEE IF YOU CAN find a way to append everything only using one line

# QUESTION 4 (incomplete)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

