from rest_framework import generics
from account.models import Post, Profile
from feed.permissions import FeedPermission
from .serializers import FeedSerializer
from rest_framework.response import Response
from post.serializers import PostSerializer

class FeedAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [FeedPermission]

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)
        followers = profile.follower.all()
        followings = [follower.following for follower in followers]
        posts_queryset = [following.posts.all() for following in followings]
        posts = [post for post in posts_queryset[0]]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)