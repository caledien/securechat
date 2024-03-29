from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
#from ..ban import middleware

urlpatterns = [
    path('', views.home, name='home'),
    path('sus_users/', views.susUsers, name='susUsers'),
    path('signup/', views.signUp, name='signup'),
    path('logout/', views.logOut, name='logout'),
    path('login/', views.logIn, name='login'),
    path('profile/', views.profile, name='profile'),
    path('banned/', views.banned,  name='banned'),
    path('getMessages/<str:rec>/', views.getMessages, name='getMessages'),
    path('sendMessage/<str:rec>/', views.sendMessage, name='sendMessage'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="chatsys/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="chatsys/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="chatsys/reset_password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="chatsys/reset_password_complete.html"), name="password_reset_complete"),
]
