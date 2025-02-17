from rest_framework import serializers

from ..models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        fields = ['user', 'product']
        read_only_fields = ['user']
