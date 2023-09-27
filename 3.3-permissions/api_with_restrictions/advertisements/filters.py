from django_filters import rest_framework as filters, DateFromToRangeFilter, FilterSet, DateTimeFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()
    status = DjangoFilterBackend()
    creator = DjangoFilterBackend()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at', 'status', 'creator']
