from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import ast


def sign_up(request, id, category):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect(f'http://127.0.0.1:8000/article/{category}/{id}')

        else:
            errors = str(form.errors.as_data)
            errors = ast.literal_eval('{' + errors.split('{')[1].rstrip('>'))

            res_list = []
            for k, v in errors.items():
                res_list.append(str(v).strip('[').strip("]").strip("'"))

            if res_list[0] == 'The two password fields didn’t match.':
                res_list[0] = 'Пароли не совпадают'

            if res_list[0] == 'A user with that username already exists.':
                res_list[0] = 'Пользователь с таким именем уже есть'

            if res_list[0] == 'The password is too similar to the username.':
                res_list[0] = 'Пароль слишком похож на имя пользователя'

            if 'This password is too short. It must contain at least 8 characters.' in res_list[0] and 'This password is too common' in res_list[0]:
                res_list[0] = 'Слишком короткий пароль (меньше 8 символов). Слишком простой пароль'

            if 'This password is too short. It must contain at least 8 characters.' in res_list[0] and 'This password is too common' not in res_list[0]:
                res_list[0] = 'Слишком короткий пароль (меньше 8 символов)'

            if 'This password is too short. It must contain at least 8 characters.'not in res_list[0] and 'This password is too common'  in res_list[0]:
                res_list[0] = 'Слишком простой пароль'



            messages.error(request, res_list[0])

    else:
        form = CreateUserForm()

    return render(request, 'accounts/sign_up.html', {'form': form, 'id': id, 'category': category})


def log_in(request, id, category):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(f'http://127.0.0.1:8000/article/{category}/{id}')

        else:
            messages.info(request, "Неверное имя пользователя или пароль")


    return render(request, 'accounts/login.html', {'id': id, 'category': category})
