from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
