from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from mezzanine.conf import settings

from cartridge.shop.models import *

class Command(BaseCommand):
    help = 'Sync reservations from external hook'

    def handle(self, *args, **options):
        for p in ReservableProduct.objects.all():
            p.update_from_hook()

