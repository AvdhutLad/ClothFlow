# Generated by Django 5.0 on 2024-03-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.IntegerField(max_length=2, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('middle_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=25)),
                ('role', models.IntegerField(max_length=1)),
                ('password', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('photo', models.BinaryField()),
                ('education', models.CharField(max_length=15)),
            ],
        ),
    ]
