from django.conf import settings
from django.db.utils import DataError

from core.service.facades import FacadeCity

from .facade_delivery_point import FacadeDeliveryPoint
from delivery_app.models import DeliveryPoint
from delivery_app.services.facades.facade_base_delivery import FacadeBaseDeliveryCdek

LOGGER = settings.LOGGER


class FacadeDeliveryPointCdek(FacadeDeliveryPoint, FacadeBaseDeliveryCdek):
    """Фасад Пункт выдачи СДЕК"""

    def create_delivery_points_task(self, delivery_points_data: dict) -> None:
        """Добавляет пункты выдачи | задача"""

        from delivery_app.tasks import create_delivery_points_task

        create_delivery_points_task.apply_async(
            args=[delivery_points_data],
            serializer="json",
        )

        return None

    def create_delivery_points(
            self,
            delivery_points_data: dict,
            is_standardized: bool = False,
            ) -> None:
        """Добавляет пункты выдачи"""

        delivery_points = delivery_points_data.get('delivery_points')
        if not delivery_points:
            return None

        if is_standardized:
            delivery_points = self.standardize_delivery_points(
                delivery_points=delivery_points,
            )

        counter = 0
        delivery_points_generator = (item for item in delivery_points)
        for delivery_point_raw in delivery_points_generator:
            delivery_point = self.create_delivery_point(
                delivery_point_raw=delivery_point_raw,
                delivery_point_type=delivery_points_data.get('delivery_point_type'),
                city_id=delivery_points_data.get('city_id'),
            )
            if not delivery_point:
                continue
            counter += 1

        LOGGER.info(f'Добавилось: {counter} пунктов выдачи')

        return None

    def create_delivery_point(
            self,
            delivery_point_raw: dict,
            delivery_point_type: int = 0,
            city_id: int = None,
            ) -> DeliveryPoint:
        """Добавляет пункт выдачи"""

        city = FacadeCity.get_city_by_id(city_id=city_id)
        if not city:
            return None

        try:
            code = delivery_point_raw.pop('code')
            uuid = delivery_point_raw.pop('uuid')
        except KeyError as er:
            LOGGER.warning(er)
            return None

        delivery_point_raw.update({'city': city, 'delivery_point_type': delivery_point_type})

        try:
            delivery_point, created = self.model.objects.update_or_create(
                code=code,
                uuid=uuid,
                defaults=delivery_point_raw,
            )
        except DataError as er:
            LOGGER.warning(er)
            return None

        LOGGER.info(f'delivery_point: {delivery_point}')

        return delivery_point

    def standardize_delivery_points(self, delivery_points: list = []) -> list:
        """Стандартизирует пункты выдачи"""

        standardized_delivery_points = []

        delivery_points_generator = (item for item in delivery_points)

        for delivery_point_raw in delivery_points_generator:

            phones = ''
            for phone in delivery_point_raw.get('phones'):
                number = phone.get('number')
                phones += f'{number},'

            dimensions = {}
            if delivery_point_raw.get('dimensions'):
                dimensions = delivery_point_raw.get('dimensions')[0]

            delivery_point = {
                'code': delivery_point_raw.get('code'),
                'uuid': delivery_point_raw.get('uuid'),

                'name': delivery_point_raw.get('name'),
                'address_comment': delivery_point_raw.get('address_comment'),
                'nearest_station': delivery_point_raw.get('nearest_station'),
                'work_time': delivery_point_raw.get('work_time'),
                'phones': phones,
                'email': delivery_point_raw.get('email'),
                'type': delivery_point_raw.get('type'),
                'owner_code': delivery_point_raw.get('owner_code'),
                'take_only': delivery_point_raw.get('take_only'),
                'is_handout': delivery_point_raw.get('is_handout'),
                'is_reception': delivery_point_raw.get('is_reception'),
                'is_ltl': delivery_point_raw.get('is_ltl'),
                'have_cashless': delivery_point_raw.get('have_cashless'),
                'have_cash': delivery_point_raw.get('have_cash'),
                'allowed_cod': delivery_point_raw.get('allowed_cod'),
                'weight_min': delivery_point_raw.get('weight_min'),
                'weight_max': delivery_point_raw.get('weight_max'),
                'postamat_width': dimensions.get('width'),
                'postamat_height': dimensions.get('height'),
                'postamat_depth': dimensions.get('depth'),
                'postal_code': delivery_point_raw.get('location').get('postal_code'),
                'latitude': delivery_point_raw.get('location').get('latitude'),
                'longitude': delivery_point_raw.get('location').get('longitude'),
                'address': delivery_point_raw.get('location').get('address'),
                'address_full': delivery_point_raw.get('location').get('address_full'),
            }
            standardized_delivery_points.append(delivery_point)

        return standardized_delivery_points
