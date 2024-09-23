from django.urls import path
from . import views
# from .views import ChangePasswordView

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('change/password/', views.change_password, name='change_password'),
    # path('change/password/', ChangePasswordView.as_view(), name='change_password'),

]