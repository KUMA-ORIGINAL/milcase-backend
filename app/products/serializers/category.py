from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['children'] = CategorySerializer(instance.children.all(), many=True).data
        return representation
