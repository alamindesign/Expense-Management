from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import DailyExpense
# Create your views here.
class ExpenseView(ListView):
    model = DailyExpense
    template_name = 'index.html'
# def list(request):
#     all_object= DailyExpense.objects.all()