from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
    lineId = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    lineId = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    INIT = 1
    DEAL = 2
    DONE = 3

    STATUS_CHOICES = (
        (INIT, "Init"),
        (DEAL, "Deal"),
        (DONE, "Done"),
    )

    seller_lineId = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer_lineId = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    order_status = models.IntegerField(choices=STATUS_CHOICES)
    picture = models.ImageField(upload_to='static/', blank=False)
    qty_can = models.IntegerField(default=0)
    qty_bottle = models.IntegerField(default=0)
    qty_glass = models.IntegerField(default=0)
    tot_price = models.IntegerField()

# class Product(models.Model):
#     owner = models.ForeignKey(Seller, on_delete=models.CASCADE)
#     productId = models.IntegerField(default=1)
#     picture = models.ImageField(upload_to='static/', blank=False)
#     qty_can = models.IntegerField(default=0)
#     qty_bottle = models.IntegerField(default=0)
#     qty_glass = models.IntegerField(default=0)
#     tot_price = models.IntegerField()
