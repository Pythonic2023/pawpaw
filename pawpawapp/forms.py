from django import forms
from django.contrib.auth.models import User
from .models import Payment

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['first_name', 'last_name', 'street_address', 'city', 'state',  'card_number', 'cvv',]
        widgets = {
            'card_number': forms.TextInput(attrs={'type': "password"})
        }