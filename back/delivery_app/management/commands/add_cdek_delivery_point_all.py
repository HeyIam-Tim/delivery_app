from django.core.management.base import BaseCommand
from django.conf import settings

import time

from core.models import City
from delivery_app.services.utils.delivery_handler import DeliveryPointsHandler

LOGGER = settings.LOGGER


class Command(BaseCommand):
    help = "Добавляет все пункты выдачи в бд"

    def handle(self, *args, **kwargs):
        cities = City.objects.filter(cdek_city_code__isnull=False).values_list('id', flat=True)

        delivery_handler = DeliveryPointsHandler()
        cities_generator = (item for item in cities)
        for city_id in cities_generator:
            delivery_handler.get_delivery_points(
                delivery_data={'city_id': city_id}
            )
            time.sleep(2)
