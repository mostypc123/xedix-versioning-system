import time as tm

with open("branches", "r") as branches_file:
    branches = branches_file.read()
    branches_list = branches.split(", ")

name = input()
if name not in branches_list:
    with open("branches", "w") as branches_file:
        branches_file.write(name + ", " + branches)

commits_file = open("commits.txt", "a")

time = tm.strftime("%H:%M %d:%m %Y")

commits_file.write("\nCurrently on branch " + name + " on " + time + "\n")
commits_file.close()

with open("status", "w") as f:
    f.write("Changed branch to " + name + "\n")