from rest_framework import serializers

from account.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'created', 'post', 'profile']
