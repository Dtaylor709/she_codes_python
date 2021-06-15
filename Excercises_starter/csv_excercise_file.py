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


colours = []

with open("colours_20.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader,None) 
    # skips the header
    for line in reader:
        # print(line)
        colours.append(line)
for colour_group in colours:
    if colour_group [4]== red:
        print(f"Red:{



# Green: 0
# Blue: 0
# Yellow: 12
