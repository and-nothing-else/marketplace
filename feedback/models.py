from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', _('open')),
        ('resolved', _('resolved')),
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    user = models.ForeignKey('user.MarketplaceUser', verbose_name=_('author'))
    subject = models.CharField(_('subject'), max_length=512)
    message = models.TextField(_('message'))
    status = models.CharField(_('status'), max_length=8, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.subject)

    def get_absolute_url(self):
        return reverse_lazy('feedback:ticket_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name=_('ticket'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    user = models.ForeignKey('user.MarketplaceUser', verbose_name=_('author'))
    message = models.TextField(_('message'))

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.message)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
