from rest_framework import serializers

from .order_item import OrderItemCreateSerializer, OrderItemListSerializer
from ..models import Order, OrderItem


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items']

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        total_price = 0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price * quantity
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total_price += price

        order.total_price = total_price
        order.apply_birthday_discount()
        order.save()
        return order


class OrderListSerializer(serializers.ModelSerializer):
    order_items = OrderItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'status', 'order_items', 'created_at', 'updated_at']
