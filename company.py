from employee import Employee

class Company:
    def __init__(self, company_name,wage_per_hour,max_days,max_hours):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.max_days = max_days
        self.max_hours = max_hours
        self.employees = []


    def add_employee(self, emp_id,emp_name):
        emp=Employee(emp_id,emp_name,self.wage_per_hour)
        self.employees.append(emp)
        print(f"Added employee {emp_id} with name {emp_name} to {self.company_name}.")
        return emp

    def get_employees(self):
        print(f"Getting employees from {self.company_name}.")
        for emp in self.employees:
            print("{:<5}{:<5}".format(emp.emp_id,emp.name))
        return self.employees

    def calculate_all_employee_monthly_wage(self):
        print("Calculating all employee monthly wage...",self.company_name)
        for emp in self.employees:
            emp.calculate_monthly_wage()