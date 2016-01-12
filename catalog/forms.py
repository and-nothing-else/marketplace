from django import forms
from .models import Item


class UserItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['category', 'active', 'name', 'article', 'price', 'old_price', 'description']
