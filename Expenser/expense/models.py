from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Expenses(models.Model):
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    time_create = models.DateTimeField(default=timezone.now)
    time_update = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title