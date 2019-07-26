from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Register
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request == "POST":
        form = UserCrateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleand_data.get('password')
            messages.success(request, "Account created for { username }!")
            login = {
                "username": username,
                "password": password,
                "message": message,
            }
            return redirect('/')
        else:
            form = UserCreationForm()
    return render(request, 'signup.html','form': form)
def posts(request):
    return render(request, 'posts.html')

def create_post(request):
    return render(request, 'create_post.html')

def validate(request):
        if request == "POST":
            form = request.POST
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleand_data.get('password')
            message.success(request, f("Account created for { username }!"))
            login = {
                "username": username,
                "password": password,
                "message": message,
            }
        else:
            form = UserCreationForm()
        return render(request, 'validate.html/',{"posted values": logindata})

