from rest_framework.permissions import BasePermission
from account.models import Profile


class FeedPermission(BasePermission):
    message = 'User can get only his feed'

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        return profile.slug == view.kwargs.get('slug')
    
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        return profile.slug == view.kwargs.get('slug')
    