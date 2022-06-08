from django.urls import path
from .views import MarkCreateAPIView, MarkDestroyAPIView, MarkUpdateAPIView, MarkListAPIView


urlpatterns = [
    path("marks/<slug:slug>/create/", MarkCreateAPIView.as_view(), name="mark_create"),
    path(
        "marks/<slug:slug>/delete/<int:pk>/",
        MarkDestroyAPIView.as_view(),
        name="mark_delete",
    ),
    path(
        "marks/<slug:slug>/edit/<int:pk>/",
        MarkUpdateAPIView.as_view(),
        name="mark_edit",
    ),
    path('marks/list/', MarkListAPIView.as_view(), name='mark_list'),
]
