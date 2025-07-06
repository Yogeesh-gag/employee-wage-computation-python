from employee import Employee
from company import Company
from multiple_companies import Multiple_Company

if __name__ == "__main__":
    # emp = Employee(input("Enter Employee ID: "), input("Enter Employee Name: "), float(input("Enter wage per hour: ")))
    # present = Employee.check_attendance(emp.name,emp.emp_id)

    # if present:
    #     emp.calculate_daily_wage(int(input("Enter how many hours worked: ")),emp.name,emp.emp_id) (UC2)
    # else:
    #     emp.calculate_daily_wage(0,emp.name,emp.emp_id)
    #
    # print("monthly wage --->", emp.cal_monthly_wage()) (UC3)
    #
    # emp.calculate_daily_wage(int(input("Enter how many hours worked: ")),emp.name,emp.emp_id)#(UC4)

    # by assuming 20 working days per month(UC5)
    # print("monthly wage --->", emp.calculate_monthly_wage())

    # by calculate the wage until condition fails(UC6)
    # print("monthly wage --->", emp.calculate_monthly_wage())

    # Creating Company
    company1=Company("Wipro",20,22,100)
    company2=Company("Bridge Labz",20,22,100)

    company1.add_employee(101,"Yogeesh")
    company2.add_employee(102,"Gagan")
    company1.add_employee(103,"Rohan")

    company1.get_employees()
    company2.get_employees()

    company1.calculate_all_employee_monthly_wage()
    company2.calculate_all_employee_monthly_wage()
