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
# class DailyExpenseAdmin(admin.ModelAdmin):
#     def balance(self):
#         return (self.income - self.total_expense)
#     # def netBalance(self):
#     #     return (('balance' + self.income)-self.total_expense)

#     list_display = ('id','date','number_of_stu','total_expense','income',balance)
#     list_filter=('date',)
# admin.site.register(DailyExpense,DailyExpenseAdmin)
