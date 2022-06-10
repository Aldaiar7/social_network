from rest_framework import generics
from account.models import Post, Profile
from feed.permissions import FeedPermission
from .serializers import FeedSerializer
from rest_framework.response import Response
from post.serializers import PostSerializer
from repost.serializers import RepostSerializer


class FeedAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [FeedPermission]

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)
        followers = profile.follower.all()
        followings = [follower.following for follower in followers]
        posts_queryset = [following.posts.all() for following in followings]
        reposts_queryset = [following.reposts.all() for following in followings]
        posts = [post for post in posts_queryset[0]]
        reposts = [repost for repost in reposts_queryset[0]]
        repost_serializer = RepostSerializer(reposts, many=True)
        serializer = PostSerializer(posts, many=True)
        serializer.res = serializer.data + repost_serializer.data
        return Response(serializer.res)
