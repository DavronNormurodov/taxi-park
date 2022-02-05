from wsgiref.util import request_uri
from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rent_cost = models.FloatField()
    

    def __str__(self):
        return self.model
