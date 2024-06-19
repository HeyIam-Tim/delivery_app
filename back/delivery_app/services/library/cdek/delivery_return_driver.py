from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryReturnInterface
from .base_cdek import BaseCdek

LOGGER = settings.LOGGER


class CdekDeliveryReturnDriver(DeliveryReturnInterface, BaseCdek):
    """СДЕК возврат заказа | двигатель"""

    def delivery_return(self, delivery_data: dict) -> dict:
        """Для отмены заказа"""

        response = self.delivery_return_api(delivery_data=delivery_data)

        return self.form_response(
            status=response.get("status"),
            data=response.get("data"),
            errors=response.get("errors")
        )

    def delivery_return_api(self, delivery_data: dict) -> dict:

        if not delivery_data.get("delivery_id") or not delivery_data.get("tariff"):
            return self.form_response(
                errors=['Данные не были переданы (order_id и tariff)'],
            )

        delivery_id = delivery_data.get("delivery_id")
        response = self.request_to_cdek(method="post",
                                        url=f"{self.cdek_base_url}/orders/{delivery_id}/clientReturn",
                                        data={"tariff_code": delivery_data.get("tariff")})

        data = None
        if not response.get("errors") and response.get("status") == self.success_status:
            cancel_status = response.get("result").get("requests")[0].get("state")
            order_uuid = response.get("result").get("entity").get("uuid")
            data = {"cancel_status": cancel_status, "order_uuid": order_uuid}

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
