from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from .models import Order
from .forms import OrderForm


class OrderFormView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'

    def get_success_url(self):
        return reverse_lazy('order:go_pay')

    def get_initial(self):
        initial = super().get_initial()
        initial['sum'] = self.request.user.tariff.price * 30
        return initial

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect(self.get_success_url())


class GoPayView(TemplateView):
    template_name = 'order/go_pay.html'
