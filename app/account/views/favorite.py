from rest_framework import viewsets, mixins
from rest_framework import permissions

from ..models import Favorite
from ..serializers import FavoriteSerializer


class FavoriteViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
