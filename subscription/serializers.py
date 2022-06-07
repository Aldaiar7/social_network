from rest_framework import exceptions
from rest_framework import serializers

from account.models import Subscription, Profile


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
