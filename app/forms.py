from tkinter import Widget
from tkinter.tix import Form
from turtle import width
from django import forms
from django.contrib.auth.models import User
from django.forms import Form, PasswordInput
from django.contrib.auth.forms import UserCreationForm

class fUserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.PasswordInput()
    def __str__(self):
        return f"{self.id} - {self.username} - {self.password}"
class fUserCreate(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Your Username',
            'required': ''
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Your Password',
            'required': ''
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Your Password',
            'required': ''
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Your Firstname',
            'required': ''
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Your Lastname',
            'required': ''
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Your Email',
            'required': ''
        })
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]