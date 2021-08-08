def displayStudent(name, age):
    print(name, age)


name = input("Enter Student's Name : ")
age = input("Enter Student's age : ")
displayStudent(name, age)

showStudent = displayStudent
showStudent(name, age)
