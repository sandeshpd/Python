from cgi import print_arguments
from threading import Timer
from time import sleep


filepath = "D:\\Practice programs\\Visual studio\Python\\courses_and_employees\\empcourses.txt"
with open(filepath, "r") as file:
    data = file.readlines()
    # print(data)
    # print(len(data))
    # print(type(data))
    # print(data[0])
    # print(data[1])
    # print(data[2])
print("--------------List of Courses and employees--------------\n")
print("List of Courses: ")
for line_of_courses in data:
    line_of_courses = line_of_courses.split("/")
    print(line_of_courses[0])
    #print(line[1:])
print("Number of Courses: ", len(data),"\n")

print("List of employees: ")
for line_of_emp in data:
    line_of_emp = line_of_emp.split("/")
    print(line_of_emp[1:])

# filepath1 = "D:\\Practice programs\\Visual studio\\Python\\courses_and_employees\\new_empcourses.txt"
# with open(filepath,"r") as new_file:
#     newdata = new_file.read()
#     print(newdata)

employeename = input("searchEmployee: ")

filepath2 = "D:\\Practice programs\\Visual studio\\Python\\courses_and_employees\\empcourses.txt"
with open(filepath2, "r") as newfile:
    data = newfile.readlines()
    for line in data:
        #line = line.split("/")
        if employeename in line:
            print("Yes! The employee is enrolled to: ", data)
            #break
        else:
            print("Enrolled in no courses.")