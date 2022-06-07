from django.urls import path
from .views import (
    CommentCreateAPIView,
    CommentDestroyAPIView,
    CommentListAPIView,
    CommentUpdateAPIView,
)

urlpatterns = [
    path(
        "comments/<slug:slug>/create/",
        CommentCreateAPIView.as_view(),
        name="create_comment",
    ),
    path(
        "comments/<slug:slug>/delete/<int:pk>/",
        CommentDestroyAPIView.as_view(),
        name="delete_comment",
    ),
    path(
        "comments/list/", CommentListAPIView.as_view(), name="list_comment"
    ),
    path(
        "comments/<slug:slug>/edit/<int:pk>/",
        CommentUpdateAPIView.as_view(),
        name="update_comment",
    ),
]
