from employee import Employee

if __name__ == "__main__":
    emp = Employee(input("Enter Employee ID: "), input("Enter Employee Name: "), float(input("Enter wage per hour: ")))
    present = Employee.check_attendance(emp.name,emp.emp_id)
    #
    # if present:
    #     emp.calculate_daily_wage(int(input("Enter how many hours worked: ")),emp.name,emp.emp_id)
    # else:
    #     emp.calculate_daily_wage(0,emp.name,emp.emp_id)

    # print("monthly wage --->", emp.cal_monthly_wage())
   
    emp.calculate_daily_wage(int(input("Enter how many hours worked: ")),emp.name,emp.emp_id)
 


