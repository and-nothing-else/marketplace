from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Tariff


def set_tariff(request, tariff_id):
    user_model = get_user_model()
    user = user_model.objects.get(id=request.user.id)
    user.tariff = Tariff.objects.get(id=tariff_id)
    user.save()
    return redirect(reverse_lazy('profile:tariff_list'))
