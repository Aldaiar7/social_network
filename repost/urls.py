from django.urls import path
from .views import RepostCreateAPIView, RepostDestroyAPIView, RepostUpdateAPIView, RepostListAPIView

urlpatterns = [
    path('reposts/<slug:slug>/create/', RepostCreateAPIView.as_view(), name='repost_create'),
    path('reposts/<slug:slug>/delete/<int:pk>/', RepostDestroyAPIView.as_view(), name='repost_delete'),
    path('reposts/<slug:slug>/edit/<int:pk>/', RepostUpdateAPIView.as_view(), name='repost_edit'),
    path('reposts/list/', RepostListAPIView.as_view(), name='repost_list'),

]
