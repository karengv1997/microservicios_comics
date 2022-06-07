from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=32, widget=(forms.TextInput()))
    age = forms.CharField(max_length=32, widget=(forms.TextInput()))

    class Meta:
        model = User
        fields = ('username', 'name', 'age', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password')