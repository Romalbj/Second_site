from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# from main.models import Articles

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("better_site:home")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {'form': form})
    # return HttpResponse('hi')

