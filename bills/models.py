from django.db import models

from django.db import models

from home.models import staff  # Import the Staff model
from inventory.models import Product  # Import the Product model

class Billing(models.Model):
    bill_no = models.AutoField(primary_key=True)  # Primary key auto increment
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)  # Foreign key from Staff model
    customer_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)
    contacts = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Foreign key from Product model
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    payment_mode = models.CharField(max_length=10,null=True)
    date_time = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.customer_name





class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 , unique=True)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name



from django.db import models


class CustomAutoField(models.AutoField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('primary_key', True)
        kwargs['unique'] = True
        kwargs['db_index'] = True
        self.sequence_start = 1000  # Set the starting value for the sequence
        super().__init__(*args, **kwargs)


class Invoice(models.Model):
    invoice_id = CustomAutoField()
    # invoice_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.FloatField(null=True)
    after_discount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    PAYMENT_STATUS_CHOICES = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
    ]
    payment_status = models.CharField(max_length=6, choices=PAYMENT_STATUS_CHOICES)
    payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "Invoice {} for {}".format(self.invoice_id,self.customer.customer_name)







class InvoiceItem(models.Model):
    invoice_item_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Invoice Item {} - {} - Invoice {}".format(self.invoice_item_id, self.product_name, self.invoice)







class Return_and_refund(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    date = models.DateField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    ACTION_CHOICES = [
        ('exchange', 'Exchange'),
        ('refund', 'Refund'),
    ]
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    reason = models.TextField()
    return_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.TextField(null=True, blank=True)
    rejected_reason = models.TextField(blank=True, null=True)
    transaction_complete_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "return and refund  {} - {} - quantity {}".format(self.transaction_id, self.product_name, self.quantity)





from django.db import models
from .models import Return_and_refund, InvoiceItem

class Defective(models.Model):
    defective_id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(Return_and_refund, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100,null=True)
    # product = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return "Defective item   {} - {} - quantity {}".format(self.defective_id, self.product_name, self.quantity)



