from django.contrib import admin
from .models import DailyExpense
# Register your models here.
class DailyExpenseAdmin(admin.ModelAdmin):
    def balance(self):
        return (self.income - self.total_expense)
        null = True
    list_display = ('id','date','number_of_stu','total_expense','income',balance)
    list_filter=('date',)
admin.site.register(DailyExpense,DailyExpenseAdmin)
