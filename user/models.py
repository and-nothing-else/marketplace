from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from tariff.models import Tariff
from logs.models import BalanceLog
from math import floor


class MarketplaceUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class MarketplaceUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    tariff = models.ForeignKey('tariff.Tariff', verbose_name=_('tariff'), blank=True, null=True)
    balance = models.FloatField(_('balanсe'), default=0)

    objects = MarketplaceUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_display_name(self):
        return self.get_full_name() or self.email

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def change_balance(self, b_sum):
        self.balance += b_sum
        self.save()

    def daily_write_off(self):
        if self.tariff:
            if self.tariff.price > 0:
                if self.tariff.price > self.balance:
                    BalanceLog.write(
                        description="""
                                    Не удалось списать средства по тарифу {}.
                                    На счету {} руб., требуется {} руб.
                                    Услуги приостановлены.
                                    """
                        .format(
                            self.tariff.name,
                            self.balance,
                            self.tariff.price
                        ),
                        sum=-self.tariff.price,
                        user=self,
                        operation_type='daily_write_off'
                    )
                    self.service_disable()
                else:
                    self.change_balance(-self.tariff.price)
                    BalanceLog.write(
                        description='Ежедневное списание по тарифу {}'.format(self.tariff.name),
                        sum=-self.tariff.price,
                        user=self,
                        operation_type='daily_write_off'
                    )

    def service_disable(self):
        # TODO: приостановить услуги
        pass

    def days_of_service_left(self):
        if self.tariff:
            if self.tariff.price > 0:
                return floor(self.balance / self.tariff.price)
        return None

    def get_catalog_items(self):
        return self.shop.item_set.all()

    def get_catalog_active_items(self):
        return self.shop.item_set.active()

    def get_catalog_active_items_count(self):
        return self.get_catalog_active_items().count()

    def has_active_items(self):
        return self.get_catalog_active_items_count() > 0

    def can_increase_active_items(self):
        return self.get_catalog_active_items_count() < self.tariff.goods

    def get_unread_messages(self):
        return self.ticket_set.filter(is_read_by_user=False)

    def get_unread_messages_link(self):
        messages = self.get_unread_messages()
        if messages.count() == 1:
            return messages[0].get_absolute_url()
        elif messages.count() > 1:
            return reverse_lazy('feedback:ticket_list')
        else:
            return None

    def has_unread_messages(self):
        return self.get_unread_messages().count() > 0

    def save(self, *args, **kwargs):
        if not self.pk:
            tariff = Tariff.objects.get_default()
            if tariff:
                self.tariff = tariff
        super().save(*args, **kwargs)
