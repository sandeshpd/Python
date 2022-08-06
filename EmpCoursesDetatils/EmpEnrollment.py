employeename = input("searchEmployee: ")

filepath2 = "D:\\Practice programs\\Visual studio\\Python\\courses_and_employees\\empcourses.txt"
with open(filepath2, "r") as newfile:
    data = newfile.readlines()
    for line in data:
        #line = line.split("/")
        if employeename in line:
            print("Yes! The Course enrolled: ", line)
            #break
        else:
            print("Enrolled in no courses.")
