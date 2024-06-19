from django.conf import settings

from core.service.data_base_services import get_city_by_name
from delivery_app.services.facades.facade_base_delivery import FacadeBaseDeliveryCdek
from delivery_app.services.utils.interfaces import DeliveryCreateInterface
from .base_cdek import BaseCdek

LOGGER = settings.LOGGER


class CdekDeliveryCreateDriver(DeliveryCreateInterface, BaseCdek, FacadeBaseDeliveryCdek):
    """СДЕК создание доставки | двигатель"""

    type = 2  # тип

    def delivery_create(self, delivery_data: dict) -> dict:
        """Для создания заказа"""

        if not delivery_data:
            return self.form_response(
                errors=['Данные не были переданы'],
            )
        if delivery_data.get("to_location") and delivery_data.get('to_location').get("city"):
            city_id = get_city_by_name(delivery_data.get('to_location').get("city"))
            to_location_code = self.get_cdek_city_code(city_id)
            if to_location_code:
                delivery_data["to_location"]["code"] = to_location_code

        if delivery_data.get("from_location") and delivery_data.get('from_location').get("city"):
            city_id = get_city_by_name(delivery_data.get('from_location').get("city"))
            from_location_code = self.get_cdek_city_code(city_id)
            if from_location_code:
                delivery_data["from_location"]["code"] = from_location_code

        delivery_data["type"] = self.type

        response = self.delivery_create_api(data=delivery_data)

        return self.form_response(
            status=response.get("status"),
            data=response.get("data"),
            errors=response.get("errors")
        )

    def delivery_create_api(self, data: dict) -> dict:
        response = self.request_to_cdek(method="post",
                                        url=f"{self.cdek_base_url}/orders",
                                        data=data)
        data = {}
        if not response.get("errors") and response.get("status") == self.success_status:
            create_status = response.get("result").get("requests")[0].get("state")
            delivery_uuid = response.get("result").get("entity").get("uuid")
            data = {"create_status": create_status, "delivery_uuid": delivery_uuid}

            return {"status": self.success_status, "data": data, "errors": []}

        return {"status": self.error_status, "data": data, "errors": response.get("errors")}

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
