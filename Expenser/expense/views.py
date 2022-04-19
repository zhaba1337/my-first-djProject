from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Страница ы')


def expenses(request):
    return HttpResponse('<h1>Страница расходов</h1>')