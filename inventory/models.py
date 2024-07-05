from django.db import models

class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    description = models.TextField()

    def __str__(self):
        return self.section_name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)  # Foreign key to Section model
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name



class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.brand_name




class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    purchase_date = models.DateField()
    supplier_name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    update_date_time = models.DateTimeField(auto_now=True)
    update_note = models.TextField()

    def __str__(self):
        return self.product_name


