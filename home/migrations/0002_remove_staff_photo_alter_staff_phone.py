# Generated by Django 5.0 on 2024-03-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='photo',
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
