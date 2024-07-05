from django.db import models


from django.utils import timezone
from home.models import staff


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    date = models.DateField()
    intime = models.TimeField()
    outtime = models.TimeField()

    ATTENDANCE_STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave'),
    ]

    attendance_status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Attendance ID: {} - Staff: {} - Date: {}".format(self.attendance_id, self.staff, self.date)

