from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    all_expense = DailyExpense.objects.all()
    return render(request,'expenseApp/index.html',{'expense': all_expense})
def Courses(request):
    course = CourseDetails.objects.all()
    return render(request,'expenseApp/course.html',{'course':course})
def Withdraws(request):
    withdraw = Withdraw.objects.all()
    return render(request,'expenseApp/withdraw.html',{'withdraw':withdraw})