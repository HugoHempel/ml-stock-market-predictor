from django.db import models

class PredictionModel(models.Model):
    PATH_CHOICES = []
    VERSIONS = []

    version = models.CharField(max_length=1, choices=VERSIONS, default='1')
    path = models.CharField(max_length=1, choices=PATH_CHOICES, default='')
    for_stock = models.CharField(max_length=200)
    acc_50 = models.DecimalField(max_digits=4, decimal_places=2)
    acc_60 = models.DecimalField(max_digits=4, decimal_places=2)
    acc_70 = models.DecimalField(max_digits=4, decimal_places=2)
    acc_80 = models.DecimalField(max_digits=4, decimal_places=2)
    acc_90 = models.DecimalField(max_digits=4, decimal_places=2)
    acc_95 = models.DecimalField(max_digits=4, decimal_places=2)
    acc_99 = models.DecimalField(max_digits=4, decimal_places=2)