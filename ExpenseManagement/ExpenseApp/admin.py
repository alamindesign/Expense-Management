from django.contrib import admin
from .models import Item,Course,Cordinator,DailyExpense,Withdraw,Balance,Student
# Register your models here.
admin.site.register(Item)
admin.site.register(Course)
admin.site.register(Cordinator)
admin.site.register(DailyExpense)
admin.site.register(Withdraw)
admin.site.register(Balance)
admin.site.register(Student)