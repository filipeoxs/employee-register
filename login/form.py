from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'email':'E-mail',
            'name':'Full Name',
            'password': 'Password',
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        labels = {
            'email':'E-mail',
            'password': 'Password',
        }
        
class ForgotForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        labels = {
            'email':'E-mail',
        }