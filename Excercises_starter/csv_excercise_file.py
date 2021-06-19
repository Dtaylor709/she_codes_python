import csv

# EXCERCICE: READING AND WRITING CSV FILES

# QUESTION 1) Write a program that reads in colours_20_simple.csv and output the colour data.

# colours = []

# with open("colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         # print(line)
#         colours.append(line)

# # print(colours)

# # for colour_group in colours:
# #     print(f"{colour_group [0]} {colour_group[1]} {colour_group[2]}")


# # QUESTION 2
# # Write a program that reads in colours_20_simple.csv and output the colour data
# #  in order English, Hex then RGB.

# colours = []

# with open("colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader,None) 
#     # skips the header
#     for line in reader:
#         # print(line)
#         colours.append(line)

# # print(colours)

# for colour_group in colours:
#     # if colour_group[0]=="RGB":
#     #     continue
#     # above two two lines another was to skip header
#     print(f"{colour_group [2]}, HEX: {colour_group[1]}, RGB: {colour_group[0]}")

# QUESTION 3)

#     Q3) Write a program that reads in colours_20.csv and output the colour data in order English, Hex then RGB.

# colours = []

# with open("colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader,None) 
#     # skips the header
#     for line in reader:
#         # print(line)
#         colours.append(line)

# # print(colours)

# for colour_group in colours:
#     # if colour_group[0]=="RGB":
#     #     continue
#     # above two two lines another was to skip header
#     print(f"{colour_group [4]}, HEX: {colour_group[2]}, RGB: {colour_group[1]}")


# QUESTION 4)

# Using the same colour csv files, write a program that outputs the number of times each of the following
# colours appear in the English Name:
# ● red
# ● green
# ● blue


# colours = []

# with open("colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader,None) 
#     # skips the header
#     for line in reader:
#         # print(line)
#         colours.append(line)
# # for colour_group in colours:
#     # print(colour_group)

# red_count = 0
# green_count = 0
# blue_count = 0
# yellow_count = 0
# for colour_group in colours:
#     # print(colour_group [4])
#     if "red" in colour_group [4]:
#         red_count = red_count + 1
        
#     if "green" in colour_group [4]:
#         green_count = green_count + 1
       
#     if "blue" in colour_group [4]:
#         blue_count = blue_count + 1
       
#     if "yellow" in colour_group [4]:
#         yellow_count = yellow_count + 1
        
# print(f"Red = {red_count}")    
# print(f"Green = {green_count}")
# print(f"Blue = {blue_count}")
# print(f"Yellow = {yellow_count}")    



# colours = []

# with open("colours_213.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader,None) 
#     # skips the header
#     for line in reader:
#         # print(line)
#         colours.append(line)
# # for colour_group in colours:
#     # print(colour_group)

# red_count = 0
# green_count = 0
# blue_count = 0
# yellow_count = 0
# for colour_group in colours:
#     if "red" in colour_group [4]:
#         red_count = red_count + 1
        
#     if "green" in colour_group [4]:
#         green_count = green_count + 1
       
#     if "blue" in colour_group [4]:
#         blue_count = blue_count + 1
       
#     if "yellow" in colour_group [4]:
#         yellow_count = yellow_count + 1
    
# print(f"Red = {red_count}")
# print(f"Green = {green_count}")
# print(f"Blue = {blue_count}")
# print(f"Yellow = {yellow_count}")

# Q5) galaxies.py contains data about 82 different galaxies and their velocities (km/sec). Using this data, output
# the galaxy with the slowest velocity, and the galaxy with the highest velocity

# galaxies = []



# with open("galaxies.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader,None) 
#     # skips the header
#     for line in reader:
#         # print(line)
#         galaxies.append(line)

# maximum_galaxy = []
# minimum_galaxy = []

# for galaxy in galaxies:
#     if not maximum_galaxy or int(galaxy[1]) > int(maximum_galaxy[1]):
#         maximum_galaxy = galaxy 
            
#     if not minimum_galaxy or int(galaxy[1]) < int(minimum_galaxy[1]):
#         minimum_galaxy = galaxy     


# print(f"Galaxy {minimum_galaxy[0]} has the min velocity of {minimum_galaxy[1]} km/sec.")
# print(f"Galaxy {maximum_galaxy[0]} has the max velocity of {maximum_galaxy[1]} km/sec.")