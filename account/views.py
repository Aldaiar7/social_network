from rest_framework import generics

from .serializers import (
    RegisterSerializer,
    ProfileUserSerializer,
    ProfileRetrieveSerializer,
    ProfileSerializer,
)
from .models import User, Profile
from .permissions import ProfileObjectPermission
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    @method_decorator(cache_page(60 * 60 * 2, key_prefix='profile'))
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileRetrieveSerializer
    queryset = Profile.objects.all()
    lookup_field = "slug"


class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileUserSerializer
    queryset = User.objects.all()
    permission_classes = [ProfileObjectPermission]


class ProfileDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProfileUserSerializer
    queryset = Profile.objects.all()
    permission_classes = [ProfileObjectPermission]


