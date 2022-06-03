from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from . import serializers
from . import models
from . import permissions


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.User.objects.all()


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProfileRetrieveSerializer
    queryset = models.Profile.objects.all()
    lookup_field = "slug"


class StatusCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.StatusSerializer
    queryset = models.Status.objects.all()
    permission_classes = [permissions.StatusPermission]


class StatusDestroyAPIView(generics.DestroyAPIView):
    serializer_class = serializers.StatusSerializer
    queryset = models.Status.objects.all()
    permission_classes = [permissions.StatusDestroyPermission]

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusListAPIView(generics.ListAPIView):
    serializer_class = serializers.StatusSerializer
    queryset = models.Status.objects.all()
