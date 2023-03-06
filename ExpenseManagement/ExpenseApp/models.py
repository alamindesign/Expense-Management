from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=50)

    def __str__(self):
        return str(self.item_name)
        
class Course(models.Model):
    course_id=models.IntegerField(default=0)
    course_name=models.CharField(max_length=100)
    course_duration= models.CharField(max_length=20)
    def __str__(self):
        return self.course_name
    
class Cordinator(models.Model):
    cordinator_id=models.IntegerField(default=0)
    cordinator_name=models.CharField(max_length=50)
    cordinator_deg=models.CharField(max_length=50)
    cordinator_nid=models.IntegerField(default=0)
    def __str__(self):
        return self.cordinator_name

class DailyExpense(models.Model):
    item_name=models.ForeignKey(Item,on_delete=models.CASCADE)
    item_price=models.IntegerField(default=0)
    item_quantity=models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    date=models.DateField()
    voucher_no = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return str(self.item_name)


class Withdraw(models.Model):
    withdraw_id=models.IntegerField(default=0)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    cordinator_id=models.ForeignKey(Cordinator,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    date=models.DateField()

class Balance(models.Model):
    date=models.DateField()
    number_of_student=models.IntegerField(default=0)
    withdraw_amount=models.PositiveIntegerField(default=0)
    total_cost=models.IntegerField(default=0)


class CourseDetails(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    cordinator_id=models.ForeignKey(Cordinator,on_delete=models.CASCADE)
    number_of_student= models.PositiveSmallIntegerField(default=0)
    course_durations = models.CharField(max_length=30, default=0)
    start_date = models.DateField(default="2023-03-01")
    end_date = models.DateField(default="2023-04-01")
    status=models.CharField(max_length=15, default='active')