from django.conf import settings

from .facade_delivery_point import FacadeDeliveryPoint

LOGGER = settings.LOGGER


class FacadeDeliveryPointYandex(FacadeDeliveryPoint):
    """Фасад Пункт выдачи | Яндекс"""

    def get_delivery_points(self, delivery_points_filter: dict) -> None:
        """Получает пункты выдачи"""

        LOGGER.info(delivery_points_filter)

        return []
