from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    all_expense = DailyExpense.objects.all()
    return render(request,'expenseApp/index.html',{'expense': all_expense})