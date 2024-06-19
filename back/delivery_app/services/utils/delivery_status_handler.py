from django.conf import settings

from .delivery_handler import BaseDeliveryHandler

LOGGER = settings.LOGGER


class StatusDeliveryHandler(BaseDeliveryHandler):
    """Работает с получением статуса заказа"""

    def __init__(self) -> None:
        _drivers = self.get_drivers()

        self.delivery_driver = _drivers.get('delivery_status_driver')()
        self.facade = _drivers.get('facade_delivery_status')()

    def delivery_status(self, delivery_data: dict) -> dict:
        """Для получения статуса заказа"""

        LOGGER.info(delivery_data)

        try:
            delivery_data._mutable = True
        except AttributeError as er:
            LOGGER.warning(er)
        delivery_data.update({'facade': self.facade})

        delivery_data_to_front = self.delivery_driver.delivery_status(
            delivery_data=delivery_data,
        )

        LOGGER.info(delivery_data_to_front)

        return delivery_data_to_front
