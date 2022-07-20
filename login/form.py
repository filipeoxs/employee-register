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
            'created_at' : 'Created At',
            'updated_at' : 'Updated At'
        }