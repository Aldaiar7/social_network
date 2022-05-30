from django.shortcuts import render
from rest_framework import generics

from .serializers import PostSerializer
from account.models import Post
from .permissions import PostPermission


class PostCreateUpdateDestroyAPIView(generics.CreateAPIView,
                                    generics.DestroyAPIView,
                                    generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [PostPermission]



class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()