from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    publishDate = models.DateField()
