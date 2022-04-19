from django.urls import path
from .views import *
 

urlpatterns = [
    path('', index),
    path('expenses', expenses),
    path('plot', post_list)
]