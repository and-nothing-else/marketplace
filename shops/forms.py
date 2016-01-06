from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'region',
            'name',
            'address',
            'map_point',
            'phone',
            'description'
        ]
