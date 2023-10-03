from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from .filters import AdvertisementFilter
from .permissions import ReadOnlyIsOwner
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        # if self.action in ["create", ]:
        #     return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'delete']:
            return [ReadOnlyIsOwner()]
        return [IsAuthenticatedOrReadOnly()]


