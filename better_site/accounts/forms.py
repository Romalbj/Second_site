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
                           (attrs={'placeholder':'Пароль',
                                   'type': 'password',
                                   'class': 'password_field'}))

    password2 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Повторите пароль',
                                   'type': 'password',
                                   'class': 'password_field'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']