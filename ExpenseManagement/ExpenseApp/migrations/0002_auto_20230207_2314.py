# Generated by Django 3.2.5 on 2023-02-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_duration',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
    ]
