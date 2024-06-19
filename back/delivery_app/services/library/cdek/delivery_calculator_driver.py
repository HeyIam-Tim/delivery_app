import time

from django.conf import settings

from delivery_app.services.utils.interfaces import DeliveryCalculatorInterface
from .base_cdek import BaseCdek

LOGGER = settings.LOGGER


class CdekDeliveryCalculatorDriver(DeliveryCalculatorInterface, BaseCdek):
    """СДЕК Расчет стоимости | двигатель"""

    delivery_point_type: int = 1
    type = 2  # Тип заказа - "доставка"

    MAINLINE_EXPRESS_SKLAD_SKLAD = {
        'tariff_code': 62,
        'tariff_name': 'Магистральный экспресс склад-склад',
    }
    MAINLINE_EXPRESS_SKLAD_DOOR = {
        'tariff_code': 122,
        'tariff_name': 'Магистральный экспресс склад-дверь',
    }
    tariffs = [MAINLINE_EXPRESS_SKLAD_SKLAD, MAINLINE_EXPRESS_SKLAD_DOOR]  # тарифы

    cdek_city_code_default = 261

    WEIGHT = 20000  # Общий вес (в граммах)

    def calculate(self, delivery_data: dict) -> dict:
        """Для расчета стоимости и сроков доставки"""

        if not delivery_data:
            return self.form_response(
                delivery_point_type=self.delivery_point_type,
                errors=['Данные не были переданы'],
            )

        city_id = delivery_data.get('city_id')

        facade = delivery_data.get('facade')
        cdek_city_code_data = facade.get_cdek_city_code(
            city_id=city_id,
        )
        cdek_city_code = cdek_city_code_data.get('cdek_city_code')
        if not cdek_city_code:
            return self.form_response(
                status=self.error_status,
                delivery_point_type=self.delivery_point_type,
                city_id=city_id,
                data={},
                errors=cdek_city_code_data.get('errors'),
            )

        delivery_data.update({'to_location_code': cdek_city_code})  # перевести id города

        calculations = []
        for tariff in self.tariffs:
            delivery_data.update({
                'tariff': tariff,
                'from_location_code': self.cdek_city_code_default,
                'weight': self.WEIGHT,
            })
            calculation = self.calculate_by_tariff(delivery_data=delivery_data)
            calculations.append(calculation)

            time.sleep(0.5)

        return self.form_response(
            status=self.success_status,
            delivery_point_type=self.delivery_point_type,
            city_id=delivery_data.get('city_id'),
            data={'calculations': calculations},
            errors=[],
        )

    def calculate_by_tariff(self, delivery_data: dict) -> dict:
        """Для расчета стоимости и сроков доставки по коду тарифа"""

        tariff = delivery_data.get('tariff')
        to_location_code = delivery_data.get('to_location_code')
        from_location_code = delivery_data.get('from_location_code')
        weight = delivery_data.get('weight')

        data_request = {
            "type": self.type,  # int: 2
            "tariff_code": tariff.get('tariff_code'),  # int: 122, 22
            "from_location": {
                "code": from_location_code,  # int: 261
            },
            "to_location": {
                "code": to_location_code,  # int: 261
            },
            "packages": [
                {
                    # // "height": 60,
                    # // "length": 60,
                    # // "width": 30,
                    "weight": weight,  # int: 20000
                }
            ]
        }

        response = self.request_to_cdek(method="post",
                                        url=f"{self.cdek_base_url}/calculator/tariff",
                                        data=data_request)

        data_response = {
            **response.get("result"),
            "tariff_code": tariff.get('tariff_code'),
            "tariff_name": tariff.get('tariff_name'),
        }

        delivery_data_to_front = data_response

        return delivery_data_to_front

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
