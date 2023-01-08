from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sus_users/', views.susUsers, name='susUsers'),
    path('signup/', views.signUp, name='signup'),
    path('logout/', views.logOut, name='logout'),
    path('login/', views.logIn, name='login'),
    path('profile/', views.profile, name='profile'),
    path('getMessages/<str:rec>/', views.getMessages, name='getMessages'),
    path('sendMessage/<str:rec>/', views.sendMessage, name='sendMessage'),
    path('reset_password/', auth_views.PasswordResetView.as_view()),
]
