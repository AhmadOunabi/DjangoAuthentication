from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )


class ActivationForm(forms.Form):
    code= forms.CharField(max_length=10)
    class Meta:
        model= Profile
        fields=('code')
        

