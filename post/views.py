from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from account import serializers

from .serializers import PostSerializer
from account.models import Post
from .permissions import PostDestroyUpdatePermission, PostPermission


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [PostPermission]


class PostDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [PostDestroyUpdatePermission]

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs["pk"])

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [PostDestroyUpdatePermission]

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs["pk"])


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
