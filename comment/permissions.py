from rest_framework.permissions import BasePermission
from account.models import Profile
from account.models import Comment


class CommentCreatePermission(BasePermission):
    message = 'User can create comments only with his profile'

    def has_permission(self, request, view):
        profile_id = request.data.get("profile")
        request_profile = Profile.objects.get(user=request.user.id)

        return request_profile.id == profile_id and (
            request_profile.slug == view.kwargs.get("slug")
        )

    def has_object_permission(self, request, view, obj):
        profile_id = request.data.get("profile")
        request_profile = Profile.objects.get(user=request.user.id)

        return request_profile.id == profile_id and (
            request_profile.slug == view.kwargs.get("slug")
        )


class CommentObjectPermission(BasePermission):
    message = 'User can delete only his comments'

    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        comment = Comment.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get('slug') == profile.slug and (profile.id == comment.profile.id)
        
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user=request.user.id)
        comment = Comment.objects.get(pk=view.kwargs.get('pk'))
        return view.kwargs.get('slug') == profile.slug and (profile.id == comment.profile.id)
