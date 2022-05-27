from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, RegisterSerializer
from .models import User

class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
