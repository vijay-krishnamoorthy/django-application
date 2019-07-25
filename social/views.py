from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request, 'signup.html')

def posts(request):
    return render(request, 'posts.html')

def create_post(request):
    return render(request, 'create_post.html')

def validate(request):
    username = request.POST['username']
    password = request.POST['password']
    logindata = dict({"username": username,"password": password})
    return render(request, 'validate.html/',{"posted values": logindata})

