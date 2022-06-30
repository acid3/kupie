from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            return redirect('/products')

    else:
        user_form = UserForm()

    context = {'user_form': user_form}

    return render(request, 'register.html', context)


def login(request):
    pass

class AdminLogin(LoginView):
    template_name = 'LoginView_form.html'
