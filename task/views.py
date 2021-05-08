from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Tasks
from .serializers import TaskSerializer
from .permissions import IsTaskOwnerOrReadOnly
from user.models import Users


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.prefetch_related('category')
    lookup_field = 'pk'
    permission_classes = (IsTaskOwnerOrReadOnly, )

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Tasks.objects.filter(owner=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)