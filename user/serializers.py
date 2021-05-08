from rest_framework import serializers

from user.models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('phone', 'username', 'first_name', 'last_name', 'email', 'birthday')