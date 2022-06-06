from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path("chat/<str:room_name>/", views.room, name="room"),
]
