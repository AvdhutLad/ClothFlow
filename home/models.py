from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class staff(models.Model):
    staff_id = models.AutoField(blank=False, null=False, primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    role = models.IntegerField(blank=False, null=False)

    password = models.CharField(max_length=16)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)

    education = models.CharField(max_length=15)

    profile_image = models.ImageField(upload_to='user_img', blank=True, null=True)

    # creating one to one relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.first_name




from django.db import models


class account_details(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE, related_name='account_details')
    account_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=200 ,null=True)
    branch_name = models.CharField(max_length=200,null=True)
    ifsc_code = models.CharField(max_length=11,null=True)
    account_no = models.CharField(max_length=16, unique=True,null=True)
    pan_no = models.CharField(max_length=10, unique=True,null=True)
    adhar_no = models.CharField(max_length=12, unique=True,null=True)

    base_salary_per_hr = models.CharField(max_length=10,  null=True)

    def __str__(self):
        return self.staff_id.first_name





# bank_details.py
from django.db import models
from .models import staff

class bank_details(models.Model):

    bank_staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    account_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=200)
    branch_name = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=11)
    account_no = models.CharField(max_length=16, unique=True)
    pan_no = models.CharField(max_length=10, unique=True)
    adhar_no = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.bank_staff_id.first_name





class leave_request(models.Model):
    leave_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)  # Foreign key to Staff model
    reason = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    review_by = models.TextField(null=True, blank=True)
    reject_reason = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.staff.first_name





