from django.db import models
from home.models import staff
from home.models import account_details
from attendance.models import Attendance
#
# class Salary(models.Model):
#     salary_id = models.AutoField(primary_key=True)
#
#     staff = models.ForeignKey(staff, on_delete=models.CASCADE)
#     account = models.ForeignKey(account_details, on_delete=models.CASCADE)
#
#     # attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
#
#     based_salary = models.IntegerField()
#     daily_working_hours = models.TimeField()
#     month_hours = models.TimeField()
#     penalty_hours = models.TimeField()
#     penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     extra_time = models.TimeField()
#     bonus_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     total_salary = models.DecimalField(max_digits=10, decimal_places=2)
#     gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.TimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "Salary ID: {} - Staff ID: {} - Date: {}".format(
#             self.salary_id , self.staff_id , self.date
#         )
#

class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    account = models.ForeignKey(account_details, on_delete=models.CASCADE)

    # attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)

    based_salary = models.IntegerField()
    daily_working_hours = models.FloatField()  # Updated to FloatField for decimal precision
    month_hours = models.FloatField()  # Updated to FloatField for decimal precision
    penalty_hours = models.FloatField()  # Updated to FloatField for decimal precision
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    extra_time = models.FloatField()  # Updated to FloatField for decimal precision
    bonus_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)  # Updated to DateField for correct date storage

    def __str__(self):
        return "Salary ID: {} - Staff ID: {} - Date: {}".format(
            self.salary_id , self.staff , self.date
        )

