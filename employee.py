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
    
