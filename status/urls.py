from django.urls import path
from .views import (
    StatusCreateAPIView,
    StatusDestroyAPIView,
    StatusListAPIView,
    StatusUpdateAPIView,
)

urlpatterns = [
    path(
        "statuses/<slug:slug>/create/",
        StatusCreateAPIView.as_view(),
        name="status_create",
    ),
    path(
        "statuses/<slug:slug>/delete/<int:pk>/",
        StatusDestroyAPIView.as_view(),
        name="status_delete",
    ),
    path(
        "statuses/<slug:slug>/edit/<int:pk>/",
        StatusUpdateAPIView.as_view(),
        name="status_edit",
    ),
    path("statuses/list/", StatusListAPIView.as_view(), name="st)atus_list"),
]
