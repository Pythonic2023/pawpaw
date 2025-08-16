from django.db import models
from django.db.models import OneToOneField
from django.contrib.auth.models import User

class Cart(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.pk}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item_name}"


class Payment(models.Model):
    #user = OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(default="", max_length=3)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)


class Products(models.Model):
    product_name = models.CharField(max_length=20)
    product_price = models.FloatField()
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return f"{self.product_name} {self.product_price}"
