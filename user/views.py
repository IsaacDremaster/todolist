from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Users
from .permissions import IsUserOwnerOrReadOnly
from .serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )

