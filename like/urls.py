from django.urls import path
from .views import LikeDestroyAPIView, LikeCreateAPIView, LikeListAPIView

urlpatterns = [
    path('likes/<slug:slug>/create/', LikeCreateAPIView.as_view(), name='like_post'),
    path('likes/<slug:slug>/delete/<int:pk>/', LikeDestroyAPIView.as_view(), name='unlike_post'),
    path('likes/list/', LikeListAPIView.as_view(), name='likes'),
]