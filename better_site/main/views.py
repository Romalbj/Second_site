from django.shortcuts import render
from .models import Articles
def home(request):
    context = {
        'articles': Articles.objects.all(),
    }
    return render(request, 'main/home.html', context)
