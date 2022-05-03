from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Expense(models.Model):#verbose_name - название на админ старнице 
    title = models.CharField(max_length=255, verbose_name='Трата на')
    amount = models.IntegerField(verbose_name='Сумма')
    time_create = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True,verbose_name = 'Дата последнего редактирования')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    
    rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name='Рубрика')
    #   ForeignKey - модель по факту создание ключа, Rubric - название первичной модели, null = Tue - разрешение на пустые значения
    # ^ on_delete = models.PROTECT - разрешение на удаление и из 2 модели PROTECT - запрещает каскадные удаления

    class Meta:# весь класс META нужен для красивого отображения названий на админ-странице 
        verbose_name_plural = 'Траты'
        verbose_name = 'объявление'
        ordering = ['-published_date']


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__ (self):#функция для корректного вывода в админ-старницу
        return self.name


    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрику'
        ordering = ['name']