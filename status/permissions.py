from rest_framework.permissions import BasePermission

from account.models import Profile, Status


class StatusPermission(BasePermission):
    message = "User can create status only for his profile."

    def has_permission(self, request, view):
        profile = Profile.objects.get(pk=request.data.get("profile"))
        return profile.user.id == request.user.id and (
            profile.slug == view.kwargs.get("slug")
        )

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(pk=request.data.get("profile"))
        return profile.user.id == request.user.id and (
            profile.slug == view.kwargs.get("slug")
        )


class StatusObjectPermission(BasePermission):
    message = "User can delete only his status."

    def has_permission(self, request, view):
        status = Status.objects.get(pk=view.kwargs.get("pk"))
        profile = Profile.objects.get(pk=status.profile.id)
        return profile.user.id == request.user.id and (
            profile.slug == view.kwargs.get("slug")
        )

    def has_object_permission(self, request, view, obj):
        status = Status.objects.get(pk=view.kwargs.get("pk"))
        profile = Profile.objects.get(pk=status.profile.id)
        return profile.user.id == request.user.id and (
            profile.slug == view.kwargs.get("slug")
        )
