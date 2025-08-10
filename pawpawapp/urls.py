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
    path("cart/delete", views.delete_cart_item, name="delete_item"),
    path("error/", views.site_error, name="site_error"),
    path("cart/payment/", views.payment, name="payment")
]