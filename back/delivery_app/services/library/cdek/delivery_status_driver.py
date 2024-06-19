from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryStatusInterface
from .base_cdek import BaseCdek

LOGGER = settings.LOGGER


class CdekDeliveryStatusDriver(DeliveryStatusInterface, BaseCdek):
    """СДЕК получение статуса заказа | двигатель"""

    def delivery_status(self, delivery_data: dict) -> dict:
        """Для получения статуса заказа"""

        response = self.delivery_status_api(delivery_data=delivery_data)

        return self.form_response(
            status=response.get("status"),
            data=response.get("data"),
            errors=response.get("errors")
        )

    def delivery_status_api(self, delivery_data: dict) -> dict:
        url = f"{self.cdek_base_url}/orders"
        params = None

        if delivery_id := delivery_data.get("delivery_id"):
            url = f"{self.cdek_base_url}/orders/{delivery_id}"
        elif cdek_number := delivery_data.get("cdek_number"):
            params = {"cdek_number": cdek_number}
        elif im_number := delivery_data.get("im_number"):
            params = {"im_number": im_number}
        else:
            return self.form_response(
                errors=['Должно быть передано одно из полей: delivery_id, cdek_number, im_number'],
            )
        response = self.request_to_cdek(method="get", url=url, params=params)

        data = None
        if not response.get("errors") and response.get("status") == self.success_status:
            requests = response.get("result").get("requests")
            statuses = response.get("result").get("entity").get("statuses")
            return {"status": self.success_status, "data": {"requests": requests, "statuses": statuses}, "errors": []}

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
