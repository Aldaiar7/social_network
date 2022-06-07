from django.urls import path
from . import views


urlpatterns = [
    path('posts/<slug:slug>/create/', views.PostCreateAPIView.as_view(), name='upload_post'),
    path('posts/list/', views.PostListAPIView.as_view(), name='post_list'),
    path('posts/<slug:slug>/delete/<int:pk>/', views.PostDestroyAPIView.as_view(), name='delete_post'),
    path('posts/<slug:slug>/edit/<int:pk>/', views.PostUpdateAPIView.as_view(), name='edit_post'),
]