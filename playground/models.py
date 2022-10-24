from django.db import models

# Create your models here.
class Event(models.Model):
    # testinig the code
    name = models.CharField("Even Name" , max_length=120)

    def __str__(self):
        return self.name