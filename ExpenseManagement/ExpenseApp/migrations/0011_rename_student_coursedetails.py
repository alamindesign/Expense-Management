# Generated by Django 3.2.5 on 2023-02-08 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0010_alter_student_end_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='CourseDetails',
        ),
    ]