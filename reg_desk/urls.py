from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('register', views.register, name='register'),
    path('check', views. check, name='check'),
    path('logout', views.logout, name='logout'),
]
