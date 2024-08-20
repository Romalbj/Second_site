from django.urls import path
from . import views

urlpatterns = [
    path('<category>/<id>', views.article_detail, name='article_detail'),
    path('like/<category>/<id>', views.like_article, name='like_article'),

]
