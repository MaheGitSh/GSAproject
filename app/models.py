from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    )
    name = models.CharField(max_length=100)
    date_time = models.DateField(auto_now_add=True)
    time = models.TimeField(default=timezone.now) 
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)

    def __str__(self):
        return self.name