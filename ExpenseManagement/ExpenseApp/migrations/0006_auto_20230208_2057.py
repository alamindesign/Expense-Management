# Generated by Django 3.2.5 on 2023-02-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0005_auto_20230208_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='end_date',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
