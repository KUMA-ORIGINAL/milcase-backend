from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class MeSerializer(serializers.ModelSerializer):
    birthday_discount = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'photo', 'birthdate', 'points', 'quantity_of_cases', 'birthday_discount')

    def get_birthday_discount(self, obj):
        return obj.get_birthday_discount()

class MeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'photo')


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'photo')
