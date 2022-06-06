from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import LikeSerializer
from .permissions import LikeCreatePermission
from account.models import Like, Post


class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [LikeCreatePermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        posts = Post.objects.filter(pk=request.data.get("post"))
        post = Post.objects.get(pk=request.data.get("post"))
        liked_by = posts.values_list("liked_by", flat=True)
        profile_id = int(request.data.get("profile"))

        if None not in liked_by:
            liked = list(liked_by)
        else:
            liked = []

        if profile_id in liked_by:
            return Response(
                "profile already liked this post", status=status.HTTP_400_BAD_REQUEST
            )
        else:
            liked.append(profile_id)
            post.liked_by.set(liked)
            post.amount_likes += 1
            post.save()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeDestroyAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeListAPIView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
