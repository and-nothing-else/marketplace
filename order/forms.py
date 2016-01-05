from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    def clean_sum(self):
        order_sum = self.cleaned_data.get('sum')
        if order_sum > 0:
            return order_sum
        raise forms.ValidationError(_('payment sum must be positive number'))

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['sum', 'paymentType']
