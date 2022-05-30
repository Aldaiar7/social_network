from django.shortcuts import render

from rest_framework import generics

from account.models import Subscription
from .serializers import SubscriptionSerializer
from .permissions import SubsctiptionPermission

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [SubsctiptionPermission]
    
