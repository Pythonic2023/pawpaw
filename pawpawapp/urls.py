from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("products/", views.products, name="products"),
    path("news/", views.news, name="news"),
    path("contacts/", views.contact, name="contact"),
    path("account/", views.account, name="account"),
    path("account/logout", views.user_logout, name="user_logout"),
]