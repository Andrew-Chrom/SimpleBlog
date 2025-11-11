from django.db import models
from datetime import datetime
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length=128)
    body  = models.TextField(max_length=1000)
    date  = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title