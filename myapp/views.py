from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate

from .models import Feature

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def index_1(request):
    return render(request, 'index_1.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Такой емейл уже есть в базе')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Пользователь с таким логином уже зарегистрирован')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Пароли не совпадают')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Неверные данные')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def project_1(request):
    return render(request, 'project.html')


def about(request):
    return render(request, 'about.html')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})