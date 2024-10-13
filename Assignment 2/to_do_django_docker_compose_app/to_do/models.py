from django.db import models

class ToDoItem(models.Model):
    text = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)