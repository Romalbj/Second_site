from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import CreateUserForm, UpdateProfileForm, PasswordChangeForm, ChangingPasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import ast
from django.contrib.auth.views import PasswordChangeView

def sign_up(request):
    global redirect_to

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect(redirect_to)

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
        redirect_to = request.GET.get('next', )


    return render(request, 'accounts/sign_up.html', {'form': form, 'next': redirect_to})


def log_in(request):
    global redirect_to

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return HttpResponse(redirect_to)
            return redirect(redirect_to)

        else:
            messages.info(request, "Неверное имя пользователя или пароль")

    redirect_to = request.GET.get('next', )
    return render(request, 'accounts/login.html', {'next': redirect_to,})

def logout_user(request):
    logout(request)
    redirect_to = request.GET.get('next',)
    return redirect(redirect_to)


def update_profile(request):
    global redirect_to

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        form = UpdateProfileForm(request.POST or None, instance=user)
        len_email = len(user.email)
        password = str('𒊹'*len_email)

        if form.is_valid():
            form.save()
            login(request, user)
            messages.success(request, "Данные профиля изменены")
            return redirect(redirect_to)
    else:
        messages.error(request, "Чтобы изменить профиль, нужно войти в аккаунт")
        return redirect(redirect_to)

    redirect_to = request.GET.get('next', )
    return render(request, 'accounts/update_profile.html', {'next': redirect_to, 'form': form, 'username': user.username, 'password': password,})


def change_password(request):
    global redirect_to

    if request.method == 'POST':
        active_user = request.user
        form = ChangingPasswordForm(user=active_user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # login(request, user)
            messages.success(request, "Пароль изменен")
            return redirect(redirect_to)

    redirect_to = request.GET.get('next', )
    active_user = request.user
    form = ChangingPasswordForm(user=active_user, data=request.POST)
    return render(request, 'accounts/change_password.html', {'form': form, 'user': active_user,})

# class ChangePasswordView(PasswordChangeView):
#     form_class = ChangingPasswordForm
#     success_url = reverse_lazy('home')
#     template_name = 'accounts/change_password.html'


