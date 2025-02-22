# Generated by Django 5.0 on 2024-03-30 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('supplier_name', models.CharField(max_length=100)),
                ('added_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100)),
                ('update_date_time', models.DateTimeField(auto_now=True)),
                ('update_note', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.section')),
            ],
        ),
    ]
