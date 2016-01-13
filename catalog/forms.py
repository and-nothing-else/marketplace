from django import forms
from sorl.thumbnail.admin.current import AdminImageWidget
from .models import *


class UserItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'active',
            'name',
            'article',
            'price',
            'old_price',
            'color',
            'size',
            'standard_size',
            'fabric',
            'description',
        ]


class UserItemCustomPropertyForm(forms.ModelForm):

    class Meta:
        model = ItemCustomProperty
        fields = ['name', 'value', 'ordering']


class UserItemPhotoForm(forms.ModelForm):

    class Meta:
        model = ItemPhoto
        fields = ['photo', 'ordering']
        widgets = {
            'photo': AdminImageWidget
        }


class UserItemSKUForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ItemSKU
        fields = [
            'color',
        ]


class UserItemSKUSizeForm(forms.ModelForm):

    class Meta:
        model = ItemSKUSize
        fields = [
            'size',
            'standard_size',
        ]


class UserItemSKUPhotoForm(forms.ModelForm):

    class Meta:
        model = ItemSKUPhoto
        fields = ['photo', 'ordering']
        widgets = {
            'photo': AdminImageWidget
        }
