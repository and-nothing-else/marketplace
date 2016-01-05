from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

PAYMENT_TYPE_CHOICES = getattr(settings, 'YANDEX_MONEY_PAYMENT_TYPE_CHOICES', (
    ('PC', "Яндекс.Деньги"),
    ('AC', "Банковская карта"),
))


class Order(models.Model):
    date = models.DateTimeField(_('date'), auto_now_add=True)
    user = models.ForeignKey('user.MarketplaceUser', verbose_name=_('user'), blank=True, null=True)
    sum = models.FloatField(_('sum'))
    paymentType = models.CharField(_('payment type'), choices=PAYMENT_TYPE_CHOICES, max_length=2, default='AC')
    paid = models.BooleanField(_('paid'), default=False)

    def __str__(self):
        return "[{}] {}: {} руб. ({})".format(self.date, self.user, self.sum, self.get_paymentType_display())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.was_paid = self.paid

    def save(self, *args, **kwargs):
        if self.paid and not self.was_paid:
            self.user.change_balance(self.sum)
        super().save(*args, **kwargs)
