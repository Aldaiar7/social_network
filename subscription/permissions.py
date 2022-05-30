from email import message
from requests import request
from rest_framework import permissions
from account.models import Profile
from account.views import ProfileListAPIView

class SubsctiptionPermission(permissions.BasePermission):
    message = "Profile that requests follow don't match profile set in request as follower"

    def has_permission(self, request, view):
        profile_id = request.data.get('follower')
        user_id = Profile.objects.get(pk=profile_id).user.id
        

        print(user_id, request.user.id)
        return user_id == request.user.id
        
    
    def has_object_permission(self, request, view, obj):
        profile_id = request.data.get('follower')
        user_id = Profile.objects.get(pk=profile_id).user.id
        

        return user_id == request.user.id