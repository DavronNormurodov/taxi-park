from statistics import mode
from django.db import models
from client.models import Clients
from cars.models import Cars
# Create your models here.
class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='orders')
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='ordered_in')
    timestamp = models.DateField(auto_created=True)
    from_date = models.DateField()
    to_date = models.DateField()
    extended = models.BooleanField(default=False)

    def __str__(self):
        return f"from {self.from_date} to {self.to_date}"

class ExtendedOrders(models.Model):
    order = models.ForeignKey(Orders, related_name='extended_form', on_delete=models.CASCADE)
    extended_from = models.DateField()
    extended_to = models.DateField()

