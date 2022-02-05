from statistics import mode
from django.db import models

class Clients(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_series = models.CharField(max_length=9)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name