from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from ..models import Order
from ..serializers import OrderSerializer

@extend_schema(tags=['Order'])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
