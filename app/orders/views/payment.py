import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

@extend_schema(tags=['Payment'])
class CreatePaymentView(APIView):

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(order.total_price * 100),  # Сумма в центах
                currency='usd',
                metadata={'order_id': order.id}
            )
            return Response({
                'client_secret': payment_intent['client_secret'],
                'order_id': order.id
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Обработка события успешной оплаты
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        order_id = payment_intent.metadata.get('order_id')

        if order_id:
            order = Order.objects.get(id=order_id)
            order.status = 'paid'
            order.save()

    return HttpResponse(status=200)
