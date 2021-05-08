from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser


class IsUserOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user