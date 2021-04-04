from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    ntn = models.CharField(max_length=200)
    stn = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    hscode = models.CharField(max_length=10)

    def __str__(self):
        return self.name
