from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Имя пользователя'}))

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

class UpdateProfileForm(UserChangeForm):

    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Имя пользователя',
                                   'class': 'username_field'}))

    email = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Почта',
                                   'class': 'email_field'}))
    class Meta:
        model = User
        fields = ['username', 'email',]

class ChangingPasswordForm(PasswordChangeForm):

    old_password = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Старый пароль',
                                  }))

    new_password1 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Новый пароль',
                                   }))

    new_password2 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Повторите новый пароль',
                                  }))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']