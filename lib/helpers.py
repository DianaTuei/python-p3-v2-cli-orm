from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name:")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')


def find_department_by_id():
    id = input("Enter the departments id: ")
    department = Department.find_by_id(id)
    print (department) if department else print(f'Department id: {id} not found')


def create_department():
    name = input("give a department name:")
    location = input("give a department location:")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department.", exc)


def update_department():
    id_ = input("Enter the department's id:")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter new name of department:")
            department.name = name
            location = input("Enter new location of department:")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)

    else:
        print(f"department id: {id_} not found")




def delete_department():
    id_ = input("Enter the department's id:")
    if department := Department.find_by_id(id_):
            department.delete()
            print(f'Department {id_} deleted')
    else:
        print(f"department id: {id_} not found")


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter employees name:")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'{name} not found')


def find_employee_by_id():
    id = input("Enter employees id:")
    employee = Employee.find_by_id(id)
    print(employee) if employee else print(f'employee {id} not found')


def create_employee():
    name = input("Enter an employee name:")
    job_title = input("Enter an employee job title:")
    department_id = input("Enter an employee department id:")

    try:
        department = Employee.create(name, job_title, department_id)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating employee.", exc)


def update_employee():
    id_ = input("Enter the employee's id:")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter new name of employee:")
            employee.name = name
            job_title = input("Enter new job title of employee:")
            employee.job_title = job_title
            department_id = input("Enter new department id of employee:")
            employee.department_id = department_id

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)

    else:
        print(f"employee id: {id_} not found")



def delete_employee():
    id_ = input("Enter the employee's id:")
    if employee := Employee.find_by_id(id_):
            employee.delete()
            print(f'Employee {id_} deleted')
    else:
        print(f"employee id: {id_} not found")


def list_department_employees():
    id_ = input("Enter the department's id:")
    department = Department.find_by_id(id_)
    if department:
        employees = Employee.get_all() 
        for employee in employees:
            if employee.department_id == department.id:
                print(employee)
    else:
        print("Department not found.")
