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
