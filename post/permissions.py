from email import message
from requests import request
from rest_framework import permissions
from account.models import Profile

class PostPermission(permissions.BasePermission):
    

    def has_permission(self, request, view):
        profile_id = int(request.data.get('profile'))
        profile_user__id = Profile.objects.get(pk=profile_id).user.id

        print(profile_user__id, request.user.id)
        return profile_user__id == request.user.id
        
    
    def has_object_permission(self, request, view, obj):
        profile_id = int(request.data.get('profile'))
        profile_user__id = Profile.objects.get(pk=profile_id).user.id

        return profile_user__id == request.user.id
        
