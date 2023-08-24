from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=50)
    priority=models.CharField(max_length=50)
    date_created=models.DateField(auto_now_add=True)
    due_date=models.DateField()


    def __str__(self):
        return self.name