import glob
import os
import random

print("Select mode:\n")
print("1: Random mode")
print("")
input_mode = str(input())

file_list = []

dir1 = os.getcwd()
#dir2 = (os.getcwd())
#dir3 = dir2.replace("\\", "/")
filename = os.path.basename(__file__)

for name in glob.glob(dir1+"/*"):
    if filename not in name and ".git" not in name and "readme.txt" not in name:
        name2 = name.replace("\\", "/")
        file_list.append(name2)

if input_mode == "1":
    name_list = []
    number_of_files = len(file_list)
    print("Select renaming method:\n")
    print("1: Short")
    print("2: 10 digits")
    print("")

    input_method = str(input())

    if input_method == "1":
        choice_list = []
        for number in range(1, number_of_files+1):
            choice_list.append(number)
        while choice_list != []:
            random_name = random.choice(choice_list)
            choice_list.remove(random_name)
            name_list.append(str(random_name))

    elif input_method == "2":
        for file in range(1, number_of_files+1):
            random_name = ""
            name_added = 0
            while name_added == 0:
                for number in range(1,11):
                    random_name += str(random.randint(1,9))
                if random_name not in name_list:
                    name_list.append(random_name)
                    name_added = 1

name_list2 = []

print("Add prefix? (y/n)")
input_prefix = str(input().lower())


if input_prefix == "y":
    print("Enter prefix:")
    prefix = str(input())
    for item in name_list:
        name_list2.append((dir1 + "/" + prefix + item).replace("\\", "/"))
else:
    for item in name_list:
        name_list2.append((dir1 + "/" + item).replace("\\", "/"))


counter = 0
for item in file_list:
    extension = os.path.splitext(item)[-1].lower()
    name_list2[counter] += extension
    counter += 1


counter = 0
for item in file_list:
    os.rename(item, name_list2[counter])
    print(f"File {item} renamed to {name_list2[counter]}")
    counter += 1



