from django.conf import settings

from delivery_app.models import DeliveryPoint
from delivery_app.services.utils.interfaces import FacadeInterface
from delivery_app.services.serializers.delivery_point_serializer import DeliveryPointSerializer

LOGGER = settings.LOGGER


class FacadeDeliveryPoint(FacadeInterface):
    """Фасад Пункт выдачи"""

    model = DeliveryPoint
    serializer = DeliveryPointSerializer

    def get_delivery_points(self, delivery_points_filter: dict) -> list:
        """Получает пункты выдачи"""

        delivery_points_filter = {
            'delivery_point_type': delivery_points_filter.get('delivery_point_type'),
            'city__id': delivery_points_filter.get('city_id'),
        }
        delivery_points = self.model.objects.filter(**delivery_points_filter)

        serializer = self.serializer(delivery_points, many=True)

        delivery_points = serializer.data

        return delivery_points
