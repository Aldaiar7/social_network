from email import message
from requests import request
from rest_framework import permissions
from account.models import Profile, Subscription


class SubscriptionPermission(permissions.BasePermission):
    message = "Profile that requests follow don't match profile set in request as follower"

    def has_permission(self, request, view):
        profile_id = request.data.get('follower')
        return profile_id == request.user.id
        
    def has_object_permission(self, request, view, obj):
        profile_id = request.data.get('follower')
        return profile_id == request.user.id


class SubscriptionSelfPermission(permissions.BasePermission):
    message = "Profile can't follow himself"

    def has_permission(self, request, view):
        follower_id = request.data.get('follower')
        following_id = request.data.get('following')
        
        return follower_id != following_id
    
    def has_object_permission(self, request, view, obj):
        follower_id = request.data.get('follower')
        following_id = request.data.get('following')
        
        return follower_id != following_id

class SubscriptionDestroyPermission(permissions.BasePermission):
    message = "Profile can delete only his follows"

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        sub = Subscription.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get('slug') == profile.slug and (profile.id == sub.follower.id)
        
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        sub = Subscription.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get('slug') == profile.slug and (profile.id == sub.follower.id)