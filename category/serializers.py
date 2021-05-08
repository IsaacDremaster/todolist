from rest_framework import serializers

from category.models import Categories

from user.models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'username')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        read_only_fields = ('owner',)

    def create(self, validated_data):
        user = self.context.get('request').user

        category = Categories.objects.create(owner=user, **validated_data)
        return category
