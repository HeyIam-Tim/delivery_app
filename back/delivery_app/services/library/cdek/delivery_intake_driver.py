from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryIntakeInterface
from .base_cdek import BaseCdek

LOGGER = settings.LOGGER


class CdekDeliveryIntakeDriver(DeliveryIntakeInterface, BaseCdek):
    """СДЕК возврат заказа | двигатель"""

    def delivery_intake(self, delivery_data: dict) -> dict:
        """Для вызова курьера"""

        response = self.delivery_intake_api(delivery_data=delivery_data)

        return self.form_response(
            status=response.get("status"),
            data=response.get("data"),
            errors=response.get("errors")
        )

    def delivery_intake_api(self, delivery_data: dict) -> dict:

        if not delivery_data:
            return self.form_response(
                errors=['Данные не были переданы'],
            )

        request_data = {
            "intake_date": delivery_data.get("intake_date"),
            "intake_time_from": delivery_data.get("intake_time_from"),
            "intake_time_to": delivery_data.get("intake_time_to")
        }
        if delivery_id := delivery_data.get("delivery_id"):
            request_data["order_uuid"] = delivery_id
        if cdek_number := delivery_data.get("cdek_number"):
            request_data["cdek_number"] = cdek_number

        response = self.request_to_cdek(method="post",
                                        url=f"{self.cdek_base_url}/intakes",
                                        data=request_data)

        data = None
        if not response.get("errors") and response.get("status") == self.success_status:
            intake_status = response.get("result").get("requests")[0].get("state")
            order_uuid = response.get("result").get("entity").get("uuid")
            data = {"intake_status": intake_status, "order_uuid": order_uuid}

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
