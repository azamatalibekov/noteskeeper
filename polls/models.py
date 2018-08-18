from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    no = 0
    yes = 0

    def __str__(self):
        return self.first_name
