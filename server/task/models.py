from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  deadline = models.DateTimeField(null=True, blank=True)
  priority = models.FloatField(default=0)
  is_completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
