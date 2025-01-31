from django.contrib import admin
from django.urls import path
from chatapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('send_message', views.send_message, name='send_message'),
    path('get_messages/<str:sender_name>/<str:receiver_name>/', views.get_messages, name='get_messages'),
    path('logout', views.logout_view, name='logout'),
]
