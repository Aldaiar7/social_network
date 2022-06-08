from rest_framework.permissions import BasePermission
from account.models import Profile, Post, Mark


class MarkPermission(BasePermission):
    message = "User can mark people only on his post"

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        post = Post.objects.get(pk=request.data.get("post"))
        return post.profile.id == profile.id and (
            profile.slug == view.kwargs.get("slug")
        )

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        post = Post.objects.get(pk=request.data.get("post"))
        return post.profile.id == profile.id and (
            profile.slug == view.kwargs.get("slug")
        )


class MarkObjectPermission(BasePermission):
    message = 'User can access only his marks'

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        mark = Mark.objects.get(pk=view.kwargs.get("pk"))
        return profile.id == mark.post.profile.id and (
            profile.slug == view.kwargs.get("slug")
        )

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        mark = Mark.objects.get(pk=view.kwargs.get("pk"))
        return profile.id == mark.post.profile.id and (
            profile.slug == view.kwargs.get("slug")
        )


class MarkSelfPermission(BasePermission):
    message = "User cannot mark himself"

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        print(profile.id)
        return profile.id != request.data.get('marked_profile')

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        print(profile.id)
        return profile.id != request.data.get('marked_profile')
