# Program to create & write in a new file & display the data of new created file.
file = open("New.txt", "w")
file.write("Hi I'm Dhruv Jain\n")
file = open("New.txt", "r")
data = file.readlines()
for line in data:
    print(line)
file.close()