from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import ChangePasswordView

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('change/password/', views.change_password, name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),


]