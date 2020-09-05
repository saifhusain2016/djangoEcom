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

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=500)

    def __str__(self):
        return self.email

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_info = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=20)
    update_desc = models.CharField(max_length=500)
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.update_desc[0:30] + "..."