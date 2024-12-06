from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  description = models.TextField()
  hours_until_deadline = models.IntegerField(default=0)
  priority_score = models.FloatField(default=0)
  
  def __str__(self):
    return self.description