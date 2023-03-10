from django.contrib import admin
from .models import Item,Course,Cordinator,DailyExpense,Withdraw,CourseDetails
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display=('id','item_name')
admin.site.register(Item,ItemAdmin)
class CourseAdmin(admin.ModelAdmin):
    list_display=('id','course_id','course_name','course_duration')
admin.site.register(Course,CourseAdmin)
class CordinatorAdmin(admin.ModelAdmin):
    list_display=('id','cordinator_id','cordinator_name','cordinator_deg','cordinator_nid')
admin.site.register(Cordinator, CordinatorAdmin)
class DailyExpenseAdmin(admin.ModelAdmin):
    list_display=('id','date','item_name','item_price','item_quantity','total')
admin.site.register(DailyExpense,DailyExpenseAdmin)
class WithdrawAdmin(admin.ModelAdmin):
    list_display=('withdraw_id','course_id','cordinator_id','amount','date')
admin.site.register(Withdraw,WithdrawAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=('course_id','cordinator_id','number_of_student','status')
admin.site.register(CourseDetails,StudentAdmin)