from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Employee

class customempregistrationform(UserCreationForm):
    email=forms.EmailField()
    employeeId=forms.CharField(max_length=10)
    class Meta:
        model=User
        fields=['username','email','employeeId','password1','password2']

class userregistrationform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
