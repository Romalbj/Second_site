from django.shortcuts import render
from django.http import HttpResponse
from main.models import Articles

def article_detail(request, id, category):

    article = Articles.objects.get(id=id)
    return render(request, 'article_detail/article_detail.html', {'article': article, 'id': id, 'category': category})
