
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('employee/')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form_login})

def register(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'login/register.html', {'form': form_usuario})

def forgot(request):
    form = PasswordResetForm()
    return render(request,'login/forget_password.html',{'form':form})