employees = []
def add_employees():
    emp_id  = input('Enter employee id: ')
    emp_name = input('Enter employee name: ')
    emp_salary = int(input('Enter employee salary: '))
    emp_age = int(input('Enter employee age: '))

    employee = {
        "ID" : emp_id,
        "Name" : emp_name,
        "Salary" : emp_salary,
        "Age" : emp_age
    }

    employees.append(employee)
    print('Employee added successfully!..\n')

def view_employees():
    if not employees:
        print("NO employee found..\n")
        return
    
    print('\n-----Employee list------')
    for emp in employees:
        print(emp)
    print()

def search_employees():
    emp_name = input("Enter emp_name to search: ")
    for emp in employees:
        if emp['Name'] == emp_name:
            print('Employee found:',emp,'\n')
            return
    print('Employee not found ..\n')

def update_employees():
    emp_id = input('Enter employee ID to update: ')
    for emp in employees:
        if emp["ID"] == emp_id:
            print('Current details:',emp)
            emp['Name'] = input('Enter new emp name: ')
            emp['Salary'] = int(input('Enter new emp salary: '))
            emp['Age'] = int(input('Enter new emp age: '))

            print('Employee update successfully!..\n')
            return
    print('Employee not found..\n')

def delete_employee():
    emp_id = input('Enter employee ID to delete: ')
    for emp in employees:
        if emp['ID'] == emp_id:
            employees.remove(emp)
            print('Employee delete successfully!..\n')
            return
    print('Employee not found..\n')

while True:
    print('================Employee Management System============')
    print('1.Add employee')
    print('2.View employee')
    print('3.Search employee')
    print('4.Update employee')
    print('5.Delete employee')
    print('6.Exit employee')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_employees()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employees()
    elif choice == '4':
        update_employees()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print('Existing program.......')
        break
    else:
        print('Invalid choice! Try again..\n')



