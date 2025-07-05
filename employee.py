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

    @staticmethod
    def get_random_working_hours():
        return random.randint(4, 12)

    def calculate_daily_wage(self, hours):
        return hours * self.wage_per_hour


    def cal_monthly_wage(self):
        monthly_wage = 0
        print(f"\nCalculating Monthly Wage for {self.name} (ID: {self.emp_id})")
        for day in range(1, 21):
            print(f"\nDay {day}:", end=" ")
            if Employee.check_attendance(self.name, self.emp_id):
                hours = Employee.get_random_working_hours()
                daily = self.calculate_daily_wage(hours)
                monthly_wage += daily
                print(f"Present | Hours: {hours} | Daily Wage: {daily}")
            else:
                print("Absent | Daily Wage: 0")
        print(f"\nTotal Monthly Wage for {self.name}: {monthly_wage}")
        return monthly_wage

    def calculate_daily_wage_match(self, hours, name, emp_id):
        status = Employee.check_attendance(name, emp_id)
        match status:
            case True:
                daily_wage = hours * self.wage_per_hour
                print(f"Present | Hours: {hours} | Daily Wage: {daily_wage}")
                return daily_wage
            case False:
                print("Absent | Daily Wage: 0")
                return 0
            case _:
                print("Invalid attendance status. Daily Wage: 0")
                return 0
