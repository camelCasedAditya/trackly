from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('home', views.register, name='dashboard'),
]