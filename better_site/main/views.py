from django.shortcuts import render
from .models import Articles
def home(request):
    context = {
        'credit': Articles.objects.filter(category='credit').order_by('-time_update')[0:5],
        'debit': Articles.objects.filter(category='debit').order_by('-time_update')[0:5],
        'savings': Articles.objects.filter(category='savings').order_by('-time_update')[0:5],
        'articles': Articles.objects.order_by('-time_update')[0:8],
    }
    return render(request, 'main/home.html', context)

def credit(request):
    context = {
        'articles': Articles.objects.filter(category='credit').order_by('-time_update'),
    }
    return render(request, 'main/credit.html', context)

def debit(request):
    context = {
        'articles': Articles.objects.filter(category='debit').order_by('-time_update'),
    }
    return render(request, 'main/debit.html', context)

def savings(request):
    context = {
        'articles': Articles.objects.filter(category='savings').order_by('-time_update'),
    }
    return render(request, 'main/savings.html', context)
