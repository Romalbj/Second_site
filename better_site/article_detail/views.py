from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Articles
from .forms import CommentForm

def article_detail(request, id, category):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post_id = id
            form.save()

            return redirect(f'http://127.0.0.1:8000/article/{category}/{id}')



    article = Articles.objects.get(id=id)
    user = request.user
    return render(request, 'article_detail/article_detail.html', {'article': article, 'id': id, 'category': category, 'form': CommentForm,
                                                                  'user': user})
