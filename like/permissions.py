from rest_framework.permissions import BasePermission

from account.models import Profile, Post


class LikeCreatePermission(BasePermission):
    message = 'user can like only with his profile.'
    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        return view.kwargs.get("slug") == profile.slug and (
            profile.id == request.data.get("profile")
        )

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        return view.kwargs.get("slug") == profile.slug and (
            profile.id == request.data.get("profile")
        )


class LikeDestroyPermission(BasePermission):
    message = 'user can delete  only his likes.'
    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        post = Post.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get("slug") == profile.slug and (
            post.profile.id == profile.id
        )

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        post = Post.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get("slug") == profile.slug and (
            post.profile.id == profile.id
        )
