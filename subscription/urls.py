
from django.urls import path

from . import views

urlpatterns = [
   path('subscribe/', views.SubscriptionCreateAPIView.as_view(), name='subscribe'),
]