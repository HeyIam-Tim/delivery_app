from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryPointsInterface
from .base_cdek import BaseCdek

LOGGER = settings.LOGGER


class CdekDeliveryPointsDriver(DeliveryPointsInterface, BaseCdek):
    """СДЕК пункты выдачи | двигатель"""

    delivery_point_type: int = 1

    def get_delivery_points(self, delivery_data: dict) -> dict:
        """Получает пункты выдачи"""

        LOGGER.info(f'CDEK: {delivery_data}')

        city_id = delivery_data.get('city_id')

        # получает id города для СДЕК
        facade = delivery_data.get('facade')
        cdek_city_code_data = facade.get_cdek_city_code(
            city_id=city_id,
        )
        cdek_city_code = cdek_city_code_data.get('cdek_city_code')
        if not cdek_city_code:
            delivery_points_data = {
                'status': self.error_status,  # self.success_status, self.error_status
                'delivery_point_type': self.delivery_point_type,
                'city_id': city_id,
                'delivery_points': [],
                'errors': cdek_city_code_data.get('errors'),
            }
            return delivery_points_data

        # пункты выдачи из апи
        delivery_points_api = self.get_delivery_points_api(
            city_code=cdek_city_code
        )

        # стандартизирует пункты выдачи
        standardized_delivery_points = facade.standardize_delivery_points(
            delivery_points=delivery_points_api.get('delivery_points'),
        )

        delivery_points_data = {
            'status': delivery_points_api.get('status'),
            'delivery_point_type': self.delivery_point_type,
            'city_id': city_id,
            'delivery_points': standardized_delivery_points,
            'errors': delivery_points_api.get('errors'),
        }

        # добавляет пункты выдачи через задачу
        facade.create_delivery_points_task(
            delivery_points_data=delivery_points_data,
        )

        return delivery_points_data

    def get_delivery_points_api(self, city_code: str) -> dict:
        """Получает пункты выдачи по апи"""

        response = self.request_to_cdek(method="get",
                                        url=f"{self.cdek_base_url}/deliverypoints",
                                        params={"city_code": city_code})
        delivery_points = []
        if not response.get("errors") and response.get("status") == self.success_status:
            delivery_points = response.get("result")

        delivery_points_api = {
            'status': response.get("status"),  # self.success_status, self.error_status
            'delivery_points': delivery_points,  # list
            'errors': response.get("errors"),  # list
        }

        return delivery_points_api

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
