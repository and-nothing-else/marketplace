from django.db import models
from django import forms
from .widjets import AddressPickerWidget


class AddressPickerField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64)
        super(AddressPickerField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': AddressPickerFormField
        }
        defaults.update(kwargs)
        return super(AddressPickerField, self).formfield(**defaults)


class AddressPickerFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({'widget': AddressPickerWidget()})
        super(AddressPickerFormField, self).__init__(*args, **kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^addresspicker\.fields\.AddressPickerField"])
except ImportError:
    pass
