from django.core.paginator import Paginator  # for paginatior
from django.shortcuts import render
from django.db.models import Sum
from itertools import groupby
# trying to sovle the problem
from datetime import datetime
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
    
    # balance = Withdraw.objects.values('date').annotate(sum = Sum('amount')).order_by('date')
    # total_cost= DailyExpense.objects.values('date').annotate(cost=Sum('item_price')).order_by('date')
    # combined_data = []
    # for date, group in groupby(list(balance) + list(total_cost), key=lambda x: x['date']):
    #     balance = sum(x['sum'] for x in group if 'amount' in x)
    #     total_cost = sum(x['cost'] for x in group if 'item_price' in x)
    #     combined_data.append({'date': date, 'withdraw_sum': balance, 'expense_sum': total_cost})
    # context = {'combined_data': combined_data}
    # main

    # balance = Withdraw.objects.values('date').annotate(sum = Sum('amount')).order_by('date')
    # total_cost= DailyExpense.objects.values('date').annotate(cost=Sum('item_price')).order_by('date')
    # context = {'balance':balance,'total_cost':total_cost}
    # return render(request,'expenseApp/dailyBalance.html',context)                   

    # chatgpt

    # Suppose you have two querysets with date-related data and sums:
    student = CourseDetails.objects.values('status').annotate(sum= Sum('number_of_student'))
    balance = Withdraw.objects.values('date').annotate(sum=Sum('amount')).order_by('date')
    total_cost = DailyExpense.objects.values('date').annotate(cost=Sum('Total')).order_by('date')

    # Create an empty dictionary to hold the combined data:
    combined_dict = {}

    # Loop over both querysets and add the data to the combined dictionary:
    for b, c in zip(balance, total_cost):
        # Get the date field value from each queryset:
        date = c['date']

        # Add the sum values from each queryset to the combined dictionary:
        combined_dict[date] = {
            'balance': b['sum'],
            'total_cost': c['cost']
        }

    # Sort the combined dictionary by the date field:
    sorted_dict = dict(sorted(combined_dict.items(), key=lambda x: x[0]))

    # The resulting sorted dictionary will look like this:
    # {datetime.date(2022, 3, 4): {'balance': 10, 'total_cost': 5},
    #  datetime.date(2022, 3, 5): {'balance': 20, 'total_cost': 10}}

    # You can then pass the sorted dictionary to your view context:
    context = {'combined_dict': sorted_dict,'student':student}
    return render(request, 'expenseApp/dailyBalance.html', context)
