from rest_framework import generics

from .serializers import (
    RegisterSerializer,
    ProfileUserSerializer,
    ProfileRetrieveSerializer,
    ProfileSerializer,
)
from .models import User, Profile
from .permissions import ProfileObjectPermission


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


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
