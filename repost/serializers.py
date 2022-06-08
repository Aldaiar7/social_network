from rest_framework import serializers

from account.models import Repost


class RepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repost
        fields = '__all__'
