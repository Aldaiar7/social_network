from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.PostCreateUpdateDestroyAPIView.as_view(), name='upload_post'),
    path('posts/', views.PostListAPIView.as_view(), name='post_list'),
]