import random

class Employee:

    def __init__(self, emp_id, name, wage_per_hour):
        self.emp_id = emp_id
        self.name = name
        self.wage_per_hour = wage_per_hour

    @staticmethod
    def check_attendance(name,emp_id):
        attendance = random.randint(0, 1)
        print(f"\nAttendance for {name} (ID: {emp_id}): {'Present' if attendance else 'Absent'}")
        return bool(attendance)

    def calculate_daily_wage(self, hours, name, emp_id):
        daily_wage = 0
        if not self.check_attendance(name, emp_id):
            print("Employee is Absent. Daily Wage: 0")
            return daily_wage
        else:
            daily_wage = hours * self.wage_per_hour
            print(f"Daily Wage: {daily_wage}")
        return daily_wage