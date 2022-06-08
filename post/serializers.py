from rest_framework import serializers
from account.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["image", "description"]


class PostListSerializer(serializers.ModelSerializer):
    comments = serializers.IntegerField(source="comments.count")

    class Meta:
        model = Post
        fields = [
            "id",
            "comments",
            "image",
            "created",
            "description",
            "amount_likes",
            "profile",
        ]
