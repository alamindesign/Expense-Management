from django.db import models

# Create your models here.
class DailyExpense(models.Model):
    serial = models.PositiveSmallIntegerField()
    date = models.DateField()
    number_of_stu = models.PositiveSmallIntegerField()
    total_expense = models.DecimalField(max_digits=10,decimal_places=2)
    income = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return str(self.date)
