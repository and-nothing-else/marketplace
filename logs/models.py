from django.db import models
from django.utils.translation import ugettext_lazy as _


class BalanceLog(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    description = models.CharField(_('description'), max_length=512)
    sum = models.FloatField(_('sum'))
    user = models.ForeignKey('user.MarketplaceUser', null=True, blank=True)
    operation_type = models.CharField(_('operation type'), max_length=15, choices=(
        ('payment', _('payment')),
        ('daily_write_off', _('daily write off')),
        ('other', _('other')),
    ), default='other')

    def __str__(self):
        return "[{}] {} | {}".format(self.created_at, self.sum, self.created_at)

    @classmethod
    def write(cls, **kwargs):
        obj = cls(**kwargs)
        obj.save()

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('operation')
        verbose_name_plural = _('balance log')
