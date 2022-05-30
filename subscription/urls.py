
from django.urls import path


from . import views

urlpatterns = [
   path('follow/<slug:slug>/', views.SubscriptionCreateAPIView.as_view(), name='follow'),
   path('unfollow/<slug:slug>/<int:pk>/', views.SubscriptionDestroyAPIView.as_view(), name='unfollow'),
   path('subscriptions/',views.SubscriptionListAPIView.as_view(), name='sub_list' )
]