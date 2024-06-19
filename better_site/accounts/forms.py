from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':' Имя пользователя'}))

    email = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Почта'}))

    password1 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Пароль'}))

    password2 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Повторите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']