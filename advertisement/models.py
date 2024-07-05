from django.db import models

class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    upload_image = models.ImageField(upload_to='Advertisement_images')
    description = models.TextField()
    clauses = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
