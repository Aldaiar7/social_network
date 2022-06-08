from rest_framework import serializers
from account.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
