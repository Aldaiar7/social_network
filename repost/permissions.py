from rest_framework.permissions import BasePermission
from account.models import Profile, Repost


class RepostPermission(BasePermission):
    message = 'User\'s profile does not match given profile'
    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        return profile.slug == view.kwargs.get('slug') and (profile.id == request.data.get('profile'))
    
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        return profile.slug == view.kwargs.get('slug') and (profile.id == request.data.get('profile'))



class RepostObjectPermission(BasePermission):
    message = 'Uer can access only his reposts'

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        repost = Repost.objects.get(pk=view.kwargs.get('pk'))

        return profile.slug == view.kwargs.get('slug') and (repost.profile.id == profile.id)
    
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        repost = Repost.objects.get(pk=view.kwargs.get('pk'))

        return profile.slug == view.kwargs.get('slug') and (repost.profile.id == profile.id)
