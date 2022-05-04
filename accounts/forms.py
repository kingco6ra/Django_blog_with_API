from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control text-center'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center'
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center'
    }))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={
        'class': 'form-control text-center'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField( label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control text-center'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center'
    }))
