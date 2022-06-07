from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profiles/register/", views.UserRegisterAPIView.as_view(), name="register"),
    path("profiles/list/", views.ProfileListAPIView.as_view(), name="profiles"),
    path(
        "profiles/<slug:slug>/retrieve/",
        views.ProfileRetrieveAPIView.as_view(),
        name="get_profile",
    ),
]
