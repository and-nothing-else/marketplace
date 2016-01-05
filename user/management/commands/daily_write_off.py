from django.core.management.base import BaseCommand
from ...models import MarketplaceUser


class Command(BaseCommand):
    help = "осуществляет ежедневные списания со счёта пользователей по текущему тарифному плану"

    def handle(self, *args, **options):
        for user in MarketplaceUser.objects.all():
            user.daily_write_off()
