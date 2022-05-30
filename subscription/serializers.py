from rest_framework import exceptions
from rest_framework import serializers

from account.models import Subscription, Profile

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
    
    def create(self, validated_data):
        follower_id = validated_data.pop('follower').id
        following_id = validated_data.pop('following').id

        
        qs = Subscription.objects.filter(follower__id=follower_id
        ).filter(following__id=following_id)

        if qs:
            raise exceptions.ValidationError({'detail':'this profile already follows another one.'})
        else:
            return Subscription.objects.create(follower=Profile.objects.get(pk=follower_id),
             following=Profile.objects.get(pk=following_id))



        


