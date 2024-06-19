from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryCalculatorInterface


LOGGER = settings.LOGGER


class YandexDeliveryCalculatorDriver(DeliveryCalculatorInterface):
    """Яндекс; Расчет стоимости | двигатель"""

    delivery_point_type = 2

    def calculate(self, delivery_data: dict) -> dict:
        """Для расчета стоимости и сроков доставки"""

        LOGGER.info(f'YANDEX: {delivery_data}')

        delivery_data_to_front = {}

        return delivery_data_to_front
