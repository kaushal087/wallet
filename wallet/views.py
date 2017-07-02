from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def logout(request):
    return render(request, 'home.html', {})

def transfer(request):
    return render(request, 'transfer.html', {})

def add(request):
    return render(request, 'add.html', {})

def passbook(request):
    return render(request, 'passbook.html', {})