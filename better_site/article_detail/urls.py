from django.urls import path
from . import views

urlpatterns = [
    path('<id>', views.test, name='test'),

]
