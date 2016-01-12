from django import forms
from sorl.thumbnail.admin.current import AdminImageWidget
from .models import Item, ItemPhoto


class UserItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'category',
            'active',
            'name',
            'article',
            'price',
            'old_price',
            'color',
            'description',
        ]


class UserItemPhotoForm(forms.ModelForm):

    class Meta:
        model = ItemPhoto
        fields = ['photo', 'ordering']
        widgets = {
            'photo': AdminImageWidget
        }
