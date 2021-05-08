from rest_framework import serializers

from .models import Tasks
from user.models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'username')


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ('owner', )

    def get_category_name(self, obj):
        return obj.category.name

    def create(self, validated_data):
        user = self.context.get('request').user

        task = Tasks.objects.create(owner=user, **validated_data)
        return task