from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import index, chatPage, loginView

urlpatterns = [
    path('chat/', index, name='home'),
    path('login/', loginView, name='login'),
    path('<str:username>/', chatPage, name='chat'),
   
]
