import django_filters
from . import models

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = models.FishingProducts
        fields = {
            'created': ['lt', 'gt'],
        }