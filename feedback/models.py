from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _


class TicketManager(models.Manager):
    def unread_by_staff(self):
        return self.get_queryset().filter(status='open', is_read_by_staff=False)


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', _('open')),
        ('resolved', _('resolved')),
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    user = models.ForeignKey('user.MarketplaceUser', verbose_name=_('author'))
    subject = models.CharField(_('subject'), max_length=512)
    message = models.TextField(_('message'))
    status = models.CharField(_('status'), max_length=8, choices=STATUS_CHOICES, default='open')

    is_read_by_user = models.BooleanField(_('is read by user'), default=True)
    is_read_by_staff = models.BooleanField(_('is read by staff'), default=False)

    objects = TicketManager()

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.subject)

    def get_absolute_url(self):
        return reverse_lazy('feedback:ticket_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-updated_at', '-created_at']
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name=_('ticket'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    user = models.ForeignKey('user.MarketplaceUser', verbose_name=_('author'))
    message = models.TextField(_('comment'))

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.message)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user == self.ticket.user:
            self.ticket.is_read_by_staff = False
        elif self.user.is_staff:
            self.ticket.is_read_by_user = False
            self.ticket.is_read_by_staff = True
        self.ticket.status = 'open'
        self.ticket.save()

    class Meta:
        ordering = ['created_at']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
