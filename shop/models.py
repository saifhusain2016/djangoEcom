from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    publishDate = models.DateField()
    category = models.CharField(max_length=100, default='')
    subcategory = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default='')

    def __str__(self):
        return self.productName
