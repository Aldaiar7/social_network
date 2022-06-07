from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import StatusSerializer
from account.models import Status
from .permissions import StatusPermission, StatusObjectPermission

class StatusCreateAPIView(generics.CreateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = [StatusPermission]


class StatusDestroyAPIView(generics.DestroyAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = [StatusObjectPermission]

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusListAPIView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusUpdateAPIView(generics.UpdateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = [StatusObjectPermission]
