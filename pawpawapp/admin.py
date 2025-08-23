from django.contrib import admin
from .models import Products, Cart, News

# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(News)