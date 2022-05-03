from email import charset
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense 
from django.utils import timezone
from django.template import loader
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import ExpenseForm
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    bbs = Expense.objects.all()[::-1]
    rubrics = Rubric.objects.all()
    context = {'bbs' : bbs, 'rubrics' : rubrics}
    return render(request, 'expense/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Expense.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bbs' : bbs, 'rubrics' : rubrics, "current_rubric" : current_rubric}

    return render(request, 'expense/rubric.html', context)

    
class ExpenseCreateView(CreateView):#наследовали класс CreateView
    template_name = 'expense/create.html'#путь к файлу с шаблоном 
    form_class = ExpenseForm#ссылка на класс-формы
    success_url = reverse_lazy('index')#адрес для перенаправления после сохранения

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

