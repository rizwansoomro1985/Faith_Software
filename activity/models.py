from django.db import models

from main.models import Customer, Item
# Create your models here.


class Job(models.Model):
    jobNo = models.IntegerField()
    jobDate = models.DateField()
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lc = models.CharField(max_length=100)
    lcDate = models.DateField()
    bl = models.CharField(max_length=100)
    blDate = models.DateField()
    igm = models.CharField(max_length=100)
    igmDate = models.DateField()
    index = models.IntegerField()
    vessel = models.CharField(max_length=100)
    description = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.FloatField()
    containers = models.IntegerField()
    size = models.IntegerField()

    dv = models.FloatField()
    invoiceValue = models.FloatField()
    exchangeRate = models.FloatField()
    valuePKR = models.FloatField()
    insurance = models.FloatField(null=True, blank=True)
    landingCharges = models.FloatField(null=True, blank=True)
    importValue = models.FloatField()
    customDuty = models.FloatField(null=True, blank=True)
    addCustomDuty = models.FloatField(null=True, blank=True)
    salesTax = models.FloatField(null=True, blank=True)
    incomeTax = models.FloatField(null=True, blank=True)
    total = models.FloatField()
    excise = models.FloatField(null=True, blank=True)
    deliveryOrder = models.FloatField(null=True, blank=True)
    terminalWharfage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.jobno + " " + client
