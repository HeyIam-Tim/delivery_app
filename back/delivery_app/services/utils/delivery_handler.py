from enum import Enum

from django.conf import settings

from delivery_app.services.facades.facade_delivery_calculator import (FacadeDeliveryCalculatorCdek,
                                                                      FacadeDeliveryCalculatorYandex)
from delivery_app.services.facades.facade_delivery_cancel.facade_delivery_cancel_cdek import FacadeDeliveryCancelCdek
from delivery_app.services.facades.facade_delivery_create.facade_delivery_create_cdek import FacadeDeliveryCreateCdek
from delivery_app.services.facades.facade_delivery_intake.facade_delivery_intake_cdek import \
    FacadeDeliveryIntakeCdek
from delivery_app.services.facades.facade_delivery_point import FacadeDeliveryPointCdek, FacadeDeliveryPointYandex
from delivery_app.services.facades.facade_delivery_return.facade_delivery_return_cdek import FacadeDeliveryReturnCdek
from delivery_app.services.facades.facade_delivery_status.facade_delivery_status_cdek import FacadeDeliveryStatusCdek
from delivery_app.services.library.cdek import CdekDeliveryPointsDriver, CdekDeliveryCalculatorDriver
from delivery_app.services.library.cdek.delivery_cancel_driver import CdekDeliveryCancelDriver
from delivery_app.services.library.cdek.delivery_create_driver import CdekDeliveryCreateDriver
from delivery_app.services.library.cdek.delivery_intake_driver import CdekDeliveryIntakeDriver
from delivery_app.services.library.cdek.delivery_return_driver import CdekDeliveryReturnDriver
from delivery_app.services.library.cdek.delivery_status_driver import CdekDeliveryStatusDriver
from delivery_app.services.library.yandex import YandexDeliveryPointsDriver, YandexDeliveryCalculatorDriver

LOGGER = settings.LOGGER


class DeliveryDrivers(Enum):
    """Список двигателей для доставки"""

    CDEK = {
        'delivery_points_driver': CdekDeliveryPointsDriver,
        'delivery_calculator_driver': CdekDeliveryCalculatorDriver,

        'facade_delivery_points': FacadeDeliveryPointCdek,
        'facade_calculator': FacadeDeliveryCalculatorCdek,

        'create_delivery_driver': CdekDeliveryCreateDriver,
        'facade_delivery_create': FacadeDeliveryCreateCdek,

        'delivery_status_driver': CdekDeliveryStatusDriver,
        'facade_delivery_status': FacadeDeliveryStatusCdek,

        'delivery_cancel_driver': CdekDeliveryCancelDriver,
        'facade_delivery_cancel': FacadeDeliveryCancelCdek,

        'delivery_return_driver': CdekDeliveryReturnDriver,
        'facade_delivery_return': FacadeDeliveryReturnCdek,

        'delivery_intake_driver': CdekDeliveryIntakeDriver,
        'facade_delivery_intake': FacadeDeliveryIntakeCdek

    }
    YANDEX = {
        'delivery_points_driver': YandexDeliveryPointsDriver,
        'delivery_calculator_driver': YandexDeliveryCalculatorDriver,

        'facade_delivery_points': FacadeDeliveryPointYandex,
        'facade_calculator': FacadeDeliveryCalculatorYandex,
    }


class BaseDeliveryHandler():
    """Работает с пунктами выдачи"""

    delivery_driver_name = settings.DELIVERY_DRIVER_NAME
    drivers = DeliveryDrivers

    def get_drivers(self) -> dict:
        """Получает двигатели для пунктов выдачи"""

        for driver in self.drivers:
            if driver.name == self.delivery_driver_name:
                delivery_drivers = driver.value
                return delivery_drivers


class DeliveryPointsHandler(BaseDeliveryHandler):
    """Работает с пунктами выдачи"""

    def __init__(self) -> None:
        _drivers = self.get_drivers()

        self.delivery_driver = _drivers.get('delivery_points_driver')()
        self.facade = _drivers.get('facade_delivery_points')()

    def get_delivery_points(self, delivery_data: dict) -> dict:
        """Получает пункты выдачи"""

        delivery_point_type = self.delivery_driver.delivery_point_type

        city_id = delivery_data.get('city_id')
        if not city_id:
            return self.delivery_driver.form_response(
                delivery_point_type=delivery_point_type,
                city_id=city_id,
                errors=['Не передан city_id'],
            )

        # получает пункты выдачи из бд
        delivery_points_db = self.facade.get_delivery_points(
            delivery_points_filter={
                'delivery_point_type': delivery_point_type,
                'city_id': city_id,
            },
        )
        if delivery_points_db:
            return self.delivery_driver.form_response(
                status=self.delivery_driver.success_status,
                delivery_point_type=delivery_point_type,
                city_id=city_id,
                data={'delivery_points': delivery_points_db},
            )

        # получает пункты выдачи по апи
        try:
            delivery_data._mutable = True
        except AttributeError as er:
            LOGGER.warning(er)
        delivery_data.update({'facade': self.facade})
        delivery_points_data = self.delivery_driver.get_delivery_points(
            delivery_data=delivery_data,
        )

        return self.delivery_driver.form_response(
            status=delivery_points_data.get('status'),
            delivery_point_type=delivery_point_type,
            city_id=city_id,
            data={'delivery_points': delivery_points_data.get('delivery_points')},
            errors=delivery_points_data.get('errors'),
        )
