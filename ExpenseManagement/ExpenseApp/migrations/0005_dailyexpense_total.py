# Generated by Django 4.1.7 on 2023-03-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ExpenseApp", "0004_remove_balance_privious_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyexpense",
            name="total",
            field=models.IntegerField(default=0),
        ),
    ]
