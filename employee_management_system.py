
class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("-" * 30)


class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee ID already exists!")
                return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, age, department, salary)
        self.employees.append(emp)
        print("Employee added successfully!")

    def display_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                emp.display()

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee Found:")
                emp.display()
                return

        print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.name = input("Enter New Name: ")
                emp.age = int(input("Enter New Age: "))
                emp.department = input("Enter New Department: ")
                emp.salary = float(input("Enter New Salary: "))
                print("Employee details updated successfully!")
                return

        print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print("Employee deleted successfully!")
                return

        print("Employee not found.")


# Creating an object
system = EmployeeManagement()

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_employee()
    elif choice == "2":
        system.display_employees()
    elif choice == "3":
        system.search_employee()
    elif choice == "4":
        system.update_employee()
    elif choice == "5":
        system.delete_employee()
    elif choice == "6":
        print("Thank you for using Employee Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
