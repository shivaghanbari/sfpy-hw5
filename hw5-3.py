def showEmployee(name, salary):
    print(name, "'s salary is ", salary)


name = input("Enter Name : ")
salary = input("Enter Salary (hint : use space then enter for null salary): ")
if salary == " ":
    showEmployee(name,9000)
else:
    showEmployee(name,salary)
