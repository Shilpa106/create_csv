from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(blank=True)
    purchase_date=models.DateField()

    def __str__(self):
       return f"{self.name}-{self.price}"

