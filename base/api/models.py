from statistics import mode
from sys import maxsize
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.name