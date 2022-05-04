from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from accounts.forms import UserRegisterForm, UserLoginForm


def signup(request):
    if request.user.is_authenticated:
        messages.error(request, 'Вы уже зарегистрировались')
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm
    return render(request, 'register.html', {'form': form})


class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm
    next_page = 'home'
    success_message = 'Вы успешно вошли'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'Вы уже вошли')
            return redirect('home')
        return super(Login, self).dispatch(request, *args, **kwargs)


class Logout(LogoutView):
    next_page = 'home'

