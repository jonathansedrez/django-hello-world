from django.db import models

# Create your models here.
class Todo(models.Model):
  todo_label = models.CharField(max_length=200)
  is_checked = models.BooleanField(default=False)