from django.urls import path
from .views import *

urlpatterns = [
    path('add/', ExpenseCreateView.as_view(), name = 'add'),
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
]