from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.UserRegisterAPIView.as_view(), name="register"),
    path("profiles/list/", views.ProfileListAPIView.as_view(), name="profiles"),
    path(
        "profiles/<slug:slug>/status/create/",
        views.StatusCreateAPIView.as_view(),
        name="status_create",
    ),
    path(
        "profiles/<slug:slug>/status/delete/<int:pk>/",
        views.StatusDestroyAPIView.as_view(),
        name="status_delete",
    ),
    path(
        "profiles/status/list/",
        views.StatusListAPIView.as_view(),
        name="status_list",
    ),
    path(
        "profiles/<slug:slug>/retrieve/",
        views.ProfileRetrieveAPIView.as_view(),
        name="get_profile",
    ),
]
