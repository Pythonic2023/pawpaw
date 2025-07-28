from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .forms import SignInForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages


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


def login(request):
    return render(request, "login.html")


def account(request):
    if request.method == "POST":
        if 'signup' in request.POST:
            user_signup = SignUpForm(request.POST, prefix="user_signup")
            user_signin = SignInForm(prefix="user_signin")
            if user_signup.is_valid():
                user_name = user_signup.cleaned_data['username']
                first_name = user_signup.cleaned_data['first_name']
                last_name = user_signup.cleaned_data['last_name']
                email = user_signup.cleaned_data['email']
                password = user_signup.cleaned_data['password']
                user = User.objects.create_user(user_name, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return render(request, "base.html")
            else:
                return render(request, "account.html", {'signupform': user_signup, 'signinform': user_signin})


        elif 'signin' in request.POST:
            if request.method == 'POST':
                if 'signin' in request.POST:
                    user_signin = SignInForm(request.POST, prefix="user_signin")
                    user_signup = SignUpForm(prefix="user_signup")
                    if user_signin.is_valid():
                        HttpResponse("Signed in")
                    else:
                        return render(request, "account.html", {'signinform': user_signin, 'signupform': user_signup})
            return HttpResponse("signin pressed")
        else:
            return None
    else:
        signin_form = SignInForm(prefix="user_signin")
        signup_form = SignUpForm(prefix="user_signup")
        context = {
            "signinform": signin_form,
            "signupform": signup_form,
        }
        return render(request,"account.html", context)