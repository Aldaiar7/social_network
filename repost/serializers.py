from rest_framework import serializers

from account.models import Repost
from post.serializers import PostSerializer


class RepostSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    
    class Meta:
        model = Repost
        fields = '__all__'
