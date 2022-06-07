from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from account.models import Subscription
from .serializers import SubscriptionSerializer
from .permissions import (
    SubscriptionPermission,
    SubscriptionDestroyPermission,
    SubscriptionSelfPermission,
    SubscriptionSinglePermission,
)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [
        SubscriptionPermission,
        SubscriptionSelfPermission,
        SubscriptionSinglePermission,
    ]


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [SubscriptionDestroyPermission]

    def get_queryset(self):
        return Subscription.objects.filter(pk=self.kwargs["pk"])

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
