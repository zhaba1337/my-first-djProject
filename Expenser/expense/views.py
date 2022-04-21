from email import charset
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense 
from django.utils import timezone
from django.template import loader
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


def viewExpense(request):
    s = 'список трат:'
    for item in Expense.objects.all():
        s += f'<h4>{item.amount} были потрачены на <i>{item.title}</i>.</h4>'
    return HttpResponse(s) 
    # content_type = 'text/plain; charset=utf-8' используется для указания кодировки utf8 для того что бы работала \n для переноса строки
    # в таком случае не будут работаь html теги



def viewExpenseWithTemplate(request):
    bbs = Expense.objects.all()
    filterCafe = Expense.objects.filter(title = 'кафе')
    filterClothing = Expense.objects.filter(title = 'одежда')
    filterTechnique = Expense.objects.filter(title = 'техника')
    return render(request, 'expense/expenseShow.html', 
        {'bbs' : bbs,'filterCafe' : filterCafe, "filterTechnique" : filterTechnique, 'filterClothing' : filterClothing})

def post_list(request):
    posts = Expense.objects.filter(title = 'title')
    return render(request, 'expense/post_list.html', {'posts': posts})