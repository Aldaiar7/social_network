from rest_framework.permissions import BasePermission
from .models import Profile


class ProfileObjectPermission(BasePermission):
    message = 'User can change only his profile'
    
    def has_permission(self, request, view):
        profile = Profile.objects.get(pk=view.kwargs.get("pk"))
        return view.kwargs.get("slug") == profile.slug and (
            profile.user.id == request.user.id
        )

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(pk=view.kwargs.get("pk"))
        return view.kwargs.get("slug") == profile.slug and (
            profile.user.id == request.user.id
        )
