# Generated by Django 5.0 on 2024-04-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_staff_email_alter_staff_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_request',
            name='reject_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
