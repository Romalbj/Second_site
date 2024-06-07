from django.urls import path
from . import views

urlpatterns = [
    path('<category>/<id>', views.test, name='article_detail'),

]
