from django.shortcuts import render, redirect
from .models import User
from .form import UserForm

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect ('login/')
    else:
        form = UserForm()
    return render(request,'login/register.html',{'form':form})

def forgot(request):
    return render(request,'login/forget_password.html')