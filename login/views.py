from django.shortcuts import render, redirect
from .form import ForgotForm, UserForm, LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request,)
    return render(request, 'login/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect ('/')
    else:
        form = UserForm()
    return render(request,'login/register.html',{'form':form})

def forgot(request):
    form = ForgotForm(request.POST)
    return render(request,'login/forget_password.html',{'form':form})