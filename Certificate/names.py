import os

# Check if the file exists and is not empty
if os.path.exists("name_list.txt") and os.stat("name_list.txt").st_size > 0:
    with open("name_list.txt", "r") as file:
        names = [name.strip() for name in file.readlines()]
else:
    names = []  # No names yet

print("Names list:", names)
