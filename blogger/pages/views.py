from django.shortcuts import render
from django.contib import messages

# Create your views here.
def base(request):
    return render(request,'base.html')
