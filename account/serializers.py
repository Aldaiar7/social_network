from rest_framework import serializers, exceptions

from django.contrib.auth.hashers import make_password
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        if self.Meta.model.objects.filter(email=attrs.get("email")).exists():
            raise exceptions.ValidationError(
                detail="User with this email already exists"
            )
        password = attrs.pop("password")
        attrs["password"] = make_password(password)
        return attrs

    class Meta:
        model = models.User
        fields = [
            "email",
            "username",
            "phone",
            "date_birth",
            "first_name",
            "second_name",
            "password",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = models.Profile
        fields = ["id", "slug", "username"]


class PostProfileSerializer(serializers.ModelSerializer):
    comments = serializers.IntegerField(source="comments.count")

    class Meta:
        model = models.Post
        fields = [
            "id",
            "amount_likes",
            "comments",
            "image",
            "description",
            "created",
        ]


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    posts = PostProfileSerializer(many=True)
    status = serializers.CharField(source="status.status")
    followers = serializers.IntegerField(source="following.count")
    followed = serializers.IntegerField(source="follower.count")

    class Meta:
        model = models.Profile
        fields = ["id", "username", "posts", "status", "followers", "followed"]
        lookup_field = "slug"


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "username",
            "email",
            "password",
            "phone",
            "date_birth",
            "first_name",
            "second_name",
        ]
