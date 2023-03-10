# Generated by Django 3.2.5 on 2023-02-08 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_student', models.PositiveSmallIntegerField(default=0)),
                ('course_durations', models.CharField(default=0, max_length=30)),
                ('start_date', models.DateField(default='2023-03-01')),
                ('end_date', models.DateField(default='2023-04-01')),
                ('status', models.CharField(default='active', max_length=15)),
                ('cordinator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpenseApp.cordinator')),
            ],
        ),
        migrations.RemoveField(
            model_name='balance',
            name='amount',
        ),
        migrations.AddField(
            model_name='balance',
            name='withdraw_amount',
            field=models.PositiveIntegerField(default=0),
        ),
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
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpenseApp.course'),
        ),
    ]
