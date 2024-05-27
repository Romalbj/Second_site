from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home1'),
    path('home', views.home, name='home'),
    path('credit', views.credit, name='credit'),
    path('debit', views.debit, name='debit'),
    path('savings', views.savings, name='savings'),

]
