from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=50)

    def _str_(self):
        return str(self.name)
        
class Course(models.Model):
    course_id=models.IntegerField(default=0)
    course_name=models.CharField(max_length=50)
    course_duration= models.DateField()
    
class Cordinator(models.Model):
    cordinator_id=models.IntegerField(default=0)
    cordinator_name=models.CharField(max_length=50)
    cordinator_deg=models.CharField(max_length=50)
    cordinator_nid=models.IntegerField(default=0)

class DailyExpense(models.Model):
    item_name=models.ForeignKey(Item,on_delete=models.CASCADE,default='item')
    item_price=models.IntegerField(default=0)
    item_quantity=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
    date=models.DateField()

    def _str_(self):
        return str(self.date)


class Withdraw(models.Model):
    withdraw_id=models.IntegerField(default=0)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    cordinator_id=models.ForeignKey(Cordinator,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    date=models.DateField()

class Balance(models.Model):
    date=models.DateField()
    number_of_student=models.IntegerField(default=0)
    privious_balance=models.IntegerField(default=0)
    amount=models.ForeignKey(Withdraw,on_delete=models.CASCADE)
    total_cost=models.IntegerField(default=0)
    net_balance=models.IntegerField(default=0)


class Student(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    cordinator_id=models.ForeignKey(Cordinator,on_delete=models.CASCADE)
    number_of_student=models.ForeignKey(Balance,on_delete=models.CASCADE)
    status=models.CharField(max_length=15)
