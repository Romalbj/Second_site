from django.shortcuts import render
from django.http import HttpResponse
from main.models import Articles

def test(request, id, category):

    article = Articles.objects.get(id=id)
    return render(request, 'article_detail/article_detail.html', {'article': article})
