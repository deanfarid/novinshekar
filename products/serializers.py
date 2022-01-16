from django.db.models import fields
from products.models import FishingProducts, feedback
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingProducts
        fields=(
            'id',
            'name',
            'descriptions',
            'price',
            'image',
            'numbers',
            'rate',
        )
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields=(
            'user',
            'rating',
            'item',
        )

from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class YourSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = FishingProducts
        fields = '__all__'