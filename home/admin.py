from django.contrib import admin
from .models import staff ,account_details , bank_details , leave_request

# Register your models here.
admin.site.register(staff)
admin.site.register(account_details)
admin.site.register(bank_details)
admin.site.register(leave_request)
