from django.forms import ModelForm
from .models import FishingProducts, PriceField

# Create the form class.
class priceform(ModelForm):
    class Meta:
        model = FishingProducts
        fields = '__all__'