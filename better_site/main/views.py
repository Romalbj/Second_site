from django.shortcuts import render
from .models import Articles
from article_detail.models import Comment
from django.db.models import Case, When
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
        'credit_amount': Articles.objects.filter(category='credit').count() * 10,
        'debit_amount': Articles.objects.filter(category='debit').count() * 10,
        'savings_amount': Articles.objects.filter(category='savings').count() * 10,
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

def search(request):

    if request.method == 'POST':

        searched = request.POST['searched']

        searched_no_register = searched.lower().split()

        request_list = []

        for word in searched_no_register:
            if len(word) > 4:
                request_list.append(word[:-2])
            else:
                request_list.append(word)

        res = []
        count = 0
        for post in Articles.objects.all():
            title = post.title.lower()
            count = 0
            for word in request_list:
                if word in title:
                    count += 1
                if count == len(request_list):
                    res.append(post.id)


        # articles = Articles.objects.filter(title__contains=searched)
        # articles = Articles.objects.filter(id=res)

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(res)])
        queryset = Articles.objects.filter(pk__in=res).order_by(preserved)

        output = False
        if len(res) >= 1:
            output = True
        else:
            output = False
        return render(request, 'main/searched_for.html', {'searched': searched, 'articles': queryset, 'post_ids': res, 'output':output, 'input': request_list,})
    else:
        return render(request, 'main/searched_for.html')
