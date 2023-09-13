""" 
Count the number of instances of class Employee

"""


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):  # Pylint: disable= missing-function-docstring
        print(f"Total Employee {Employee.empCount}")

    def display_employee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.display_employee()
emp2.display_employee()

print("Total Employee %d" % Employee.empCount)

# The above program defines a class Employee. The class has a constructor __init__() which takes two arguments
# name and salary and stores them in corresponding properties. The class also has a method display_count()
# to display the number of employees, and another method display_employee() to display the employee details.


# initializa a list of 4 employees
employees = [Employee("Zara", 2000), Employee(
    "Manni", 5000), Employee("Pablo", 10000), Employee("John", 20000)]

# print the list of employees
print("List of employees:")
for employee in employees:
    employee.display_employee()

# print the number of employees
print("Total Employee %d" % Employee.empCount)
