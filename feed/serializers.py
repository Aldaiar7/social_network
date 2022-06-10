from requests import post
from rest_framework import serializers
from account.models import Post


class FeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = post
        fields = '__all__'
