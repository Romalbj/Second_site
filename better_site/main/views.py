from django.shortcuts import render
from .models import Articles
def home(request):
    context = {
        'articles': Articles.objects.all(),
    }
    return render(request, 'main/home.html', context)

def credit(request):
    context = {
        'articles': Articles.objects.all(),
    }
    return render(request, 'main/credit.html', context)

def debit(request):
    context = {
        'articles': Articles.objects.all(),
    }
    return render(request, 'main/debit.html', context)

def savings(request):
    context = {
        'articles': Articles.objects.all(),
    }
    return render(request, 'main/savings.html', context)
