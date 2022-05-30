from rest_framework import generics


from . import serializers
from . import models



class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.User.objects.all()



class ProfileListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()

