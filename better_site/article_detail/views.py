from django.shortcuts import render
from django.http import HttpResponse

def test(request, id):
    # return render(request, 'article_detail/test.html')
    return HttpResponse(id)
