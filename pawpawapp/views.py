from django.shortcuts import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


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

# Serves account template, displays signin and signup forms if user is not logged in.
def account(request):
    if request.method == "POST":
        if request.POST.get('form_type') == 'signup':
            return signup(request)

        elif request.POST.get('form_type') == 'signin':
           return signin(request)
        else:
            return None
    else:
        form = AuthenticationForm()
        signup_form = SignUpForm(prefix="user_signup")
        context = {
            "signupform": signup_form,
            "signinform": form,
        }
        return render(request, "account.html", context)


def signup(request):
    user_signup = SignUpForm(request.POST, prefix="user_signup")
    user_signin = AuthenticationForm()
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


def signin(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(f"{user} AUTHENTICATED")
        if user is not None:
            login(request, user)
            return HttpResponse(f"logged in as {user}")
        else:
            user_signup = SignUpForm(request.POST, prefix="user_signup")
            user_signin = AuthenticationForm()
            return render(request, "account.html", {'signupform': user_signup, 'signinform': user_signin})
    else:
        user_signup = SignUpForm(request.POST, prefix="user_signup")
        user_signin = AuthenticationForm()
        return render(request, "account.html", {'signupform': user_signup, 'signinform': user_signin})


def user_logout(request):
    logout(request)
    return HttpResponse("logged out")