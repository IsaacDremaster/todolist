from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Categories
from .permissions import IsCategoryOwnerOrReadOnly
from .serializers import CategorySerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.prefetch_related('owner')
    lookup_field = 'pk'
    permission_classes = (IsCategoryOwnerOrReadOnly, )

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Categories.objects.filter(owner=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
