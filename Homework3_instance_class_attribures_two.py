class Employee:
    # Class variable
    company_name = "ABC Corp"
    total_employees = 0

    def __init__(self, name, role):
        self.name = name  # Instance variable
        self.role = role  # Instance variable
        Employee.total_employees += 1

    def get_employee_info(self):
        return f"Name: {self.name}, Role: {self.role}, Company: {Employee.company_name}"

# Create instances of the Employee class
employee1 = Employee("Alice", "Manager")
employee2 = Employee("Bob", "Developer")
employee3 = Employee("Herman", "Developer")

# Print employee information
print(employee1.get_employee_info())
print(employee2.get_employee_info())

# Print total number of employees
print(f"Total Employees: {Employee.total_employees}")
