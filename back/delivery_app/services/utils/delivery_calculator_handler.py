from django.conf import settings

from .delivery_handler import BaseDeliveryHandler

LOGGER = settings.LOGGER


class DeliveryCalculatorHandler(BaseDeliveryHandler):
    """Работает с расчетом доставки"""

    def __init__(self) -> None:
        _drivers = self.get_drivers()

        self.delivery_driver = _drivers.get('delivery_calculator_driver')()
        self.facade = _drivers.get('facade_calculator')()

    def calculate(self, delivery_data: dict) -> dict:
        """Для расчета стоимости и сроков доставки"""

        LOGGER.info(delivery_data)

        try:
            delivery_data._mutable = True
        except AttributeError as er:
            LOGGER.warning(er)
        delivery_data.update({'facade': self.facade})

        delivery_data_to_front = self.delivery_driver.calculate(
            delivery_data=delivery_data,
        )

        LOGGER.info(delivery_data_to_front)

        return delivery_data_to_front
