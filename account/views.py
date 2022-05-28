from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from .permissions import PostPermission


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.User.objects.all()


class PostCreateUpdateDestroyAPIView(generics.CreateAPIView,
                                    generics.DestroyAPIView,
                                    generics.UpdateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    permission_classes = [PostPermission]