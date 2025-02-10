from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeViewSet
from djoser.views import UserViewSet

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/me/', MeViewSet.as_view()),
    path('auth/users/', UserViewSet.as_view({'post': 'create'})),
    path('auth/users/activation/', UserViewSet.as_view({'post': 'activation'})),
    path('auth/users/resend_activation/', UserViewSet.as_view({'post': 'resend_activation'})),
    path('auth/users/reset_password/', UserViewSet.as_view({'post': 'reset_password'})),
    path('auth/users/reset_password_confirm/', UserViewSet.as_view({'post': 'reset_password_confirm'})),
    path('', include('djoser.urls.jwt')),
]
