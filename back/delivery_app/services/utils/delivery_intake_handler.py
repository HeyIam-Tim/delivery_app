from django.conf import settings

from .delivery_handler import BaseDeliveryHandler

LOGGER = settings.LOGGER


class IntakeDeliveryHandler(BaseDeliveryHandler):
    """Работает с оформлением возврата заказа"""

    def __init__(self) -> None:
        _drivers = self.get_drivers()

        self.delivery_driver = _drivers.get('delivery_intake_driver')()
        self.facade = _drivers.get('facade_delivery_intake')()

    def delivery_intake(self, delivery_data: dict) -> dict:
        """Для оформления возврата заказа"""

        LOGGER.info(delivery_data)

        try:
            delivery_data._mutable = True
        except AttributeError as er:
            LOGGER.warning(er)
        delivery_data.update({'facade': self.facade})

        delivery_data_to_front = self.delivery_driver.delivery_intake(
            delivery_data=delivery_data,
        )

        LOGGER.info(delivery_data_to_front)

        return delivery_data_to_front