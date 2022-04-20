from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense 
from django.utils import timezone
# Create your views here.

def index(request):
    return HttpResponse('Страница ы')


def expenses(request):
    return HttpResponse('<h1>Страница расходов</h1>')

def post_list(request):
    posts = Expense.objects.filter(title = 'title')
    return render(request, 'expense/post_list.html', {'posts': posts})

def yes(request):
    return HttpResponse('<h1>правильно! Пидорас</h1>')

def no(request):
    return HttpResponse('<h1>Ошибаешься, ты пидорас.</h1>')