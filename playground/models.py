from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField("Even Name" , max_length=120)

    def __str__(self):
        return self.name