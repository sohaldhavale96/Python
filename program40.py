# When you open file to write, it is important to close file as well.
users = open("user1.txt","w")
users.write("this is text.")
users.close()

# colours list
colours = ["yellow\n","red\n","blue\n"]
colors = open("colors.txt","w")
colors.writelines(colours)
colors.close()

# read data
with open("colors.txt", "r") as read_colours:
    for color in read_colours:
        print(color.strip())