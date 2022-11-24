from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class CreateUser(UserCreationForm):
    dob=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","dob","password1","password2"]