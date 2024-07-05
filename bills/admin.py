from django.contrib import admin
from .models import Billing ,Customer , Invoice ,InvoiceItem , Return_and_refund , Defective

# Register your models here.
admin.site.register(Billing)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Return_and_refund)
admin.site.register(Defective)