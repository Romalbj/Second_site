from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Articles
from .forms import CommentForm
from django.urls import reverse

def article_detail(request, id, category):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post_id = id
            form.save()

            return redirect(f'http://127.0.0.1:8000/article/{category}/{id}')



    article = Articles.objects.get(id=id)
    total_likes = article.likes.count()
    user = request.user

    liked = False
    if article.likes.filter(id=request.user.id).exists():
        liked = True

    return render(request, 'article_detail/article_detail.html', {'article': article, 'id': id, 'category': category, 'form': CommentForm,
                                                                  'user': user, 'total_likes': total_likes, 'liked': liked, })
def like_article(request, id, category):
    post = get_object_or_404(Articles, id=request.POST.get('article_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True



    return redirect(f'http://127.0.0.1:8000/article/{category}/{id}')