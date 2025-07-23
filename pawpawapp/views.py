from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return render(request, "base.html")


def cart(request):
    return render(request, "cart.html")


def products(request):
    return render(request, "products.html")


def news(request):
    return render(request, "news.html")


def contact(request):
    return render(request, "contact.html")