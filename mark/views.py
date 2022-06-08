from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from account.models import Mark
from .serializers import MarkSerializer
from .permissions import MarkPermission
from .permissions import MarkObjectPermission
from .permissions import MarkSelfPermission


class MarkCreateAPIView(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [MarkPermission, MarkSelfPermission]


class MarkDestroyAPIView(generics.DestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [MarkObjectPermission]

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(args, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MarkUpdateAPIView(generics.UpdateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [MarkObjectPermission, MarkSelfPermission]


class MarkListAPIView(generics.ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
