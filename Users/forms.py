from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegisterForm(UserCreationForm):
    Email = forms.EmailField()
    Firstname=forms.CharField(max_length=10)
    Lastname=forms.CharField(max_length=10)
    Phone=forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username','Firstname', 'Lastname','Phone','Email', 'password1', 'password2']