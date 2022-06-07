from xml.dom.minidom import Comment
from rest_framework import serializers
from account.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"
