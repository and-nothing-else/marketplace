from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from ...models import MarketplaceUser
from dateutil.relativedelta import relativedelta


class Command(BaseCommand):
    help = "осуществляет ежедневные списания со счёта пользователей по текущему тарифному плану"

    def handle(self, *args, **options):
        days_free = int(settings.DAYS_FREE) or 30
        now = timezone.now()
        reg_date = now - relativedelta(days=days_free)

        for user in MarketplaceUser.objects.filter(date_joined__lt=reg_date):
            user.daily_write_off()
