from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet
from orders.views.payment import CreatePaymentView, stripe_webhook

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-payment/<int:order_id>/', CreatePaymentView.as_view(), name='create-payment'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
]
