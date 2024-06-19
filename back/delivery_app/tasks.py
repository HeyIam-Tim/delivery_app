from django.conf import settings
from celery import shared_task

from .services.facades.facade_delivery_point import FacadeDeliveryPointCdek


LOGGER = settings.LOGGER

facade = FacadeDeliveryPointCdek


@shared_task
def create_delivery_points_task(delivery_points_data: dict) -> None:
    """Добавляет пункты выдачи | задача"""

    facade_delivery_point = facade()
    facade_delivery_point.create_delivery_points(
        delivery_points_data=delivery_points_data,
    )

    return None
