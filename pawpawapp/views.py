from django.shortcuts import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm, PaymentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Cart, CartItem


def index(request):
    return render(request, "base.html")


def cart(request):
    if not request.user.is_authenticated:
        path = request.path # Get path from request object
        formatted_path = path.replace("/", "") # Format to a user friendly string with no slashes
        context = {
            'error': formatted_path,
        }
        return render(request, "loginrequired.html", context)
    else:
        # Get Users cart items if there is any and send them to template
        authenticated_user = User.objects.get(username=request.user)
        try:
            Cart.objects.get(user=authenticated_user)
            cart_item_instance = CartItem.objects.all()
            cart_items = cart_item_instance
            context = {'cart': cart_items,
                       }
            return render(request, "cart.html", context)
        except Cart.DoesNotExist:
            empty_cart = "Cart empty"
            context = {
                'error_message': empty_cart,
            }

            return render(request, "siteerror.html", context)


def delete_cart_item(request):
    if request.method == "POST":
        cart_item = request.POST.get("item_id")
        try:
            cart_item_instance = CartItem.objects.get(id=cart_item)
            cart_item_instance.delete()
            cart_items_list = CartItem.objects.all()
            cart_items = cart_items_list
            context = {
                'cart': cart_items,
            }
            return render(request, "cart.html", context)
        except CartItem.DoesNotExist:
            delete_cart_item_error = "Oops, we had trouble with your cart items."
            return site_error(request, delete_cart_item_error)
    else:
        error_message = "We seem to be have trouble, please try again."
        return site_error(request, error_message)


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
            "signinform": form,
            "signupform": signup_form,
        }
        return render(request, "account.html", context)


def signup(request):
    user_signup = SignUpForm(request.POST, prefix="user_signup")
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
        return render(request, "signupsuccess.html", {'user': user_name})
    else:
        user_signin = AuthenticationForm()
        return render(request, "account.html", {'signupform': user_signup, 'signinform': user_signin})


def signin(request):
    user_signin = AuthenticationForm(request, data=request.POST)
    print(f"Form type: {request.POST.get('form_type')}")
    if request.POST.get('form_type') == 'signin':
        if user_signin.is_valid():
            username = user_signin.cleaned_data['username']
            password = user_signin.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(f"{user} AUTHENTICATED")
            if user is not None:
                login(request, user)
                return HttpResponse(f"logged in as {user}")
            else:
                user_signup = SignUpForm()
                user_signin = AuthenticationForm()
                return render(request, "account.html", {'signupform': user_signup, 'signinform': user_signin})
        else:
            user_signup = SignUpForm()
            return render(request, "account.html", {'signinform': user_signin, 'signupform': user_signup})
    else:
        user_signup = SignUpForm()
        user_signin = AuthenticationForm(request.POST, prefix=user_signin)
        return render(request, "account.html", {'signupform': user_signup, 'signinform': user_signin})


def user_logout(request):
    logout(request)
    return HttpResponse("logged out")


def site_error(request, error_message):
    context = {
        'error_message': error_message,
    }

    return render(request, "siteerror.html", context)


def payment(request):
    context = {
        'paymentform': PaymentForm
    }
    return render(request, "payment.html", context)


def payment_complete(request):
    cart_items = CartItem.objects.all()
    user = request.user
    context = {
        'cart_items': cart_items,
        'user': user,
    }
    user_object = User.objects.get(username=request.user)
    user_id = user_object.pk
    cart_object = Cart.objects.get(user=user_id)
    cart_object.delete()
    return render(request, "paymentcomplete.html", context)