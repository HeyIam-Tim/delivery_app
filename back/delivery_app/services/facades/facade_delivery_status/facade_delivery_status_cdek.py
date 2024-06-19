from django.conf import settings

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryStatusCdek(FacadeInterface):
    """Фасад для получения статуса заказа"""

    pass
