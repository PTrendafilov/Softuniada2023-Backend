from django.db import models
from datetime import datetime
# Create your models here.
class Project(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    pay = models.CharField(max_length=100, default=0)
    bids = models.IntegerField(default=0)
    is_it_done = models.BooleanField(default=False)
    creator = models.CharField(max_length=100, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'
