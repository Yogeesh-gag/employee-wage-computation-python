from employee import Employee

if __name__ == "__main__":
    emp = Employee(input("Enter Employee ID: "), input("Enter Employee Name: "), float(input("Enter wage per hour: ")))
    present = Employee.check_attendance(emp.name,emp.emp_id)



