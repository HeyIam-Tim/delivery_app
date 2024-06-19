from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryCreateInterface

LOGGER = settings.LOGGER


class YandexOrderCreateDriver(DeliveryCreateInterface):
    """Яндекс создание доставки | двигатель"""

    type = 2  # тип

    def delivery_create(self, delivery_data: dict) -> dict:
        """Для создания доставки"""

        return {}

    def delivery_create_api(self, data: dict) -> dict:
        return {}

    def form_response(
        self,
        status: str = 'error',
        data: dict = {},
        errors: list = [],
    ) -> dict:
        """Формирует ответ"""

        delivery_data = {
            'status': status,  # str: self.success_status, self.error_status
            'data': data,  # dict
            'errors': errors,  # list
        }
        return delivery_data
