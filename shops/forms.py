from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'region',
            'name',
            'description',
            'phone',
            'address',
            'map_point',
        ]
