from django.shortcuts import render

from .models import *


# Create your views here.
def Home(request):
    #================== date filter start ======================#
    if request.method == 'POST':
        date = request.POST.get('date')
        if date == "":
            filtered_data = DailyExpense.objects.all()
            return render(request, 'expenseApp/index.html',{'expense':filtered_data})
        filtered_data = DailyExpense.objects.filter(date__exact=date)
        return render(request, 'expenseApp/index.html',{'expense':filtered_data})
#================== date filter end ======================#
    all_expense = DailyExpense.objects.all()
    return render(request,'expenseApp/index.html',{'expense': all_expense})



def Courses(request):
    course = CourseDetails.objects.all()
    return render(request,'expenseApp/course.html',{'course':course})



def Withdraws(request):
    #================== date filter start ======================#
    
    if request.method == 'POST':
        date = request.POST.get('date')
        if date == "":
            filtered_data = Withdraw.objects.all()
            return render(request, 'expenseApp/withdraw.html',{'withdraw':filtered_data, 'date':date})
        filtered_data = Withdraw.objects.filter(date__exact=date)
        return render(request, 'expenseApp/withdraw.html',{'withdraw':filtered_data, 'date':date})
#================== date filter end ======================#
    withdraw = Withdraw.objects.all()
    return render(request,'expenseApp/withdraw.html',{'withdraw':withdraw})



def DailyBalance(request):
        #================== date filter start ======================#
    if request.method == 'POST':
        date = request.POST.get('date')
        if date == "":
            filtered_data = Balance.objects.all()
            return render(request, 'expenseApp/dailyBalance.html',{'balance':filtered_data})
        filtered_data = Balance.objects.filter(date__exact=date)
        return render(request, 'expenseApp/dailyBalance.html',{'balance':filtered_data})
#================== date filter end ======================#
    balance = Balance.objects.all()
    return render(request,'expenseApp/dailyBalance.html',{'balance':balance})