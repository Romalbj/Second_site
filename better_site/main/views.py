from django.shortcuts import render
from .models import Articles
from article_detail.models import Comment
def home(request):

    latest_article = Articles.objects.latest('time_create')
    latest_article_content = latest_article.content
    latest_article_content = latest_article_content.replace('<p>', '').replace('</p>', '').replace('<h3>', '').replace('</h3>', '')

    comments_amount = {}

    for post in Articles.objects.all():
        counter = post.comments.all().count()
        comments_amount[post.id] = counter


    max_comments_post_id = max(comments_amount, key=comments_amount.get)
    hottest_article = Articles.objects.get(id=max_comments_post_id)
    hottest_article_content = hottest_article.content
    hottest_article_content = hottest_article_content.replace('<p>', '')\
        .replace('</p>', '').replace('<h3>', '').replace('</h3>', '')

    context = {
        'credit': Articles.objects.filter(category='credit').order_by('-time_update')[0:5],
        'debit': Articles.objects.filter(category='debit').order_by('-time_update')[0:5],
        'savings': Articles.objects.filter(category='savings').order_by('-time_update')[0:5],
        'articles': Articles.objects.order_by('-time_update')[1:8],
        'latest_article': Articles.objects.order_by('-time_update')[:1],
        'latest_article_content': latest_article_content,
        'hottest_article': hottest_article,
        'hottest_article_article_content': hottest_article_content,
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
