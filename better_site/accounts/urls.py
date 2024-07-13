from django.urls import path
from . import views

urlpatterns = [
    path('<category>/<id>/signup/', views.sign_up, name='sign_up'),
    path('<category>/<id>/login/', views.log_in, name='login'),

]