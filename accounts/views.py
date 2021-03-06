from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, AccountAuthenticationForm

# Create your views here.


def home_view(request):
    return render(request, 'base.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def account_authentication(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')