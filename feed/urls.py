from django.urls import path
from .views import FeedAPIView


urlpatterns = [
   path('feed/<slug:slug>/', FeedAPIView.as_view(), name='feed_list')
]
