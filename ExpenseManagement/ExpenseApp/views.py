from django.core.paginator import Paginator  # for paginatior
from django.shortcuts import render
from django.db.models import Sum
from .models import *

# Create your views here.


def Home(request):
#================== date filter start ======================#
    if request.method == 'POST':
        date = request.POST.get('date')
        date2 =request.POST.get('date2')
        if date == "" or date2 =="":
            
            all_expense_list = DailyExpense.objects.all()
            # Create a paginator object with a specified number of objects per page
            paginator = Paginator(all_expense_list, 10)
            
            # Get the page number from the request query string, default to 1
            page_number = request.GET.get('page', 1)
            
            # Use the paginator to get the specified page
            expense = paginator.get_page(page_number)
            return render(request,'expenseApp/index.html',{'expense': expense})
        filtered_data = DailyExpense.objects.filter(date__range=[date,date2])
        return render(request, 'expenseApp/index.html',{'expense':filtered_data})
#================== date filter end ======================#
    all_expense_list = DailyExpense.objects.all()
    # Create a paginator object with a specified number of objects per page
    paginator = Paginator(all_expense_list, 10)
    
    # Get the page number from the request query string, default to 1
    page_number = request.GET.get('page', 1)
    
    # Use the paginator to get the specified page
    expense = paginator.get_page(page_number)
    return render(request,'expenseApp/index.html',{'expense': expense})



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
    balance = Withdraw.objects.values('date').annotate(sum = Sum('amount')).order_by('date')
    total_cost= DailyExpense.objects.values('date').annotate(cost=Sum('item_price'))
    context = {'balance':balance,'total_cost':total_cost}
    return render(request,'expenseApp/dailyBalance.html',context)