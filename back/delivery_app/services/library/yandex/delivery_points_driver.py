from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryPointsInterface


LOGGER = settings.LOGGER


class YandexDeliveryPointsDriver(DeliveryPointsInterface):
    """Доставка Яндекс"""

    delivery_point_type = 2

    def get_delivery_points(self, delivery_data: dict) -> dict:
        """Получает пункты выдачи"""

        LOGGER.info(f'YANDEX: {delivery_data}')

        delivery_data_to_front = {}

        return delivery_data_to_front

    def form_response(
            self,
            status: str = 'error',
            delivery_point_type: int = 0,
            city_id: int = 0,
            data: dict = {},
            errors: list = [],
            ) -> dict:
        """Формирует ответ"""

        delivery_points_data = {
            'status': status,  # str: self.success_status, self.error_status
            'delivery_point_type': delivery_point_type,  # int
            'city_id': city_id,  # int
            'data': data,  # dict
            'errors': errors,  # list
        }
        return delivery_points_data
