from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status 
from account.models import Repost
from .serializers import RepostSerializer
from .permissions import RepostPermission, RepostObjectPermission


class RepostCreateAPIView(generics.CreateAPIView):
    queryset = Repost.objects.all()
    serializer_class = RepostSerializer
    permission_classes = [RepostPermission]


class RepostDestroyAPIView(generics.DestroyAPIView):
    queryset = Repost.objects.all()
    serializer_class = RepostSerializer
    permission_classes = [RepostObjectPermission]

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RepostUpdateAPIView(generics.UpdateAPIView):
    queryset = Repost.objects.all()
    serializer_class = RepostSerializer
    permission_classes = [RepostObjectPermission]


class RepostListAPIView(generics.ListAPIView):
    queryset = Repost.objects.all()
    serializer_class = RepostSerializer
