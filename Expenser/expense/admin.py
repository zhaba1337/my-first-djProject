from django.contrib import admin
from .models import Expense
from .models import Rubric
# Register your models here.


class Expense_admin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'rubric','time_create', 'published_date')#простой вывод
    list_display_links = ('title', 'amount')# вывод и форматирование в  гиперссылки
    search_fields = ('title', 'amount', "time_create") # поисковые стркои
admin.site.register(Expense, Expense_admin)
admin.site.register(Rubric)