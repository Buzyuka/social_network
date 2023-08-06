from django import forms
from django.contrib.auth import views as auth_views
from . import views


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
