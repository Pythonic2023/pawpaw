from django.db import models
from django.db.models import OneToOneField
from django.contrib.auth.models import User

class Cart(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item_name}"