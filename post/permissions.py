from email import message
from requests import request
from rest_framework import permissions
from account.models import Profile, Post

class PostPermission(permissions.BasePermission):
    

    def has_permission(self, request, view):
        profile_id = int(request.data.get('profile'))
        profile_user__id = Profile.objects.get(pk=profile_id).user.id
        return profile_user__id == request.user.id
        
    def has_object_permission(self, request, view, obj):
        profile_id = int(request.data.get('profile'))
        profile_user__id = Profile.objects.get(pk=profile_id).user.id
        return profile_user__id == request.user.id
        

class PostDestroyUpdatePermission(permissions.BasePermission):
    message = "only author of post can change it."

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        post = Post.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get('slug') == profile.slug and (profile.id == post.profile.id)
        
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        post = Post.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get('slug') == profile.slug and (profile.id == post.profile.id)