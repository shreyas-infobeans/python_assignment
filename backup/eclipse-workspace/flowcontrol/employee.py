n = int(input("Enter employee number "))
employees = {}
for i in range(n):
    name = input("Enter employee name")
    salary = input("Enter salary")
    employees[name] = salary
while True:
    name = input("Enter employee name")
    salary = employees.get(name,-1)
    if(salary==-1):
        print("Employee does not exist")
    else:
        print("Salary of employee is", salary)    
    choice = input("Do you want to continue? y or n")
    if(choice=="n"):
        break
    